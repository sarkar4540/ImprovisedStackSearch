import json
import re
from flask import Flask

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, SentimentOptions
from stackapi import StackAPI
import networkx as nx

nlu = NaturalLanguageUnderstandingV1(
    iam_apikey="1A3R_SmipU_wkdOjJRwSxZPmn6dIgriROn4M6zngTR3v", version="2018-11-16",
    url="https://gateway-lon.watsonplatform.net/natural-language-understanding/api")

app = Flask(__name__)


def get_keywords(sentence):
    """Fetches the keywords of the given sentence"""
    keywords = []
    response = nlu.analyze(
        text=sentence,
        language="en",
        features=Features(keywords=KeywordsOptions())).get_result()
    for keyword_obj in response['keywords']:
        keywords.append(keyword_obj["text"].lower())
    return separate_elements(keywords)


def space_separated_elements(array):
    """Converts the question_tags array to a space separated string"""
    string = ""
    for element in array:
        string = string + element + " "

    return string


def separate_elements(array):
    list_a = []
    for element in array:
        list_a.extend(element.split(" "))
    return list_a


def get_questions_stackoverflow(query, mincount):
    """Fetches the questions from Stackoverflow API using the query provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("search/advanced", q=query, sort="relevance", accepted=True, pagesize=mincount, max_pages=1,
                      filter="withbody")
    return res


def get_answers_stackoverflow(question_id):
    """Fetches the answers from Stackoverflow API using the question_id provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("questions/{ids}/answers", ids=[question_id], sort="votes", filter="withbody")
    return res


def get_comments_stackoverflow(answer_id):
    """Fetches the comments from Stackoverflow API using the answer_id provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("answers/{ids}/comments", ids=[answer_id], sort="creation", filter="withbody")
    return res


def analyse_sentiment(sentence):
    """Calculates the compound index of the sentence using NLTK Vader SentimentAnalyser"""
    response = nlu.analyze(
        text=sentence,
        language="en",
        sentiment=SentimentOptions()).get_result()
    return float(response["sentiment"]["document"]["score"])


@app.route("/<int:answer_limit>/<question>")
def search(answer_limit, question):
    question_tags = get_keywords(question)
    print("Extracted tags: ", end="")
    print(question_tags)
    edges = []
    nodes = []
    questions = {}
    result_json_q = (get_questions_stackoverflow(
        space_separated_elements(question_tags), answer_limit))
    if "items" in result_json_q:
        print("Got " + str(len(result_json_q["items"])) + " questions... processing.")
        questions_tags = {}
        for question_b in result_json_q["items"]:
            tags = list(set(get_keywords(question_b["title"])) | set(question_b["tags"]))
            questions_tags[question_b["question_id"]] = tags
            questions[question_b["question_id"]] = question_b;
            for tag1 in tags:
                if not (tag1 in nodes):
                    nodes.append(tag1)
                for tag2 in tags:
                    if not (tag1 is tag2):
                        edges.append((tag1, tag2))
    print("Ranking questions... ", end="")
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    probable_paths = []
    for source in re.findall(r'\w+', question):
        for destination in question_tags:
            if not (source is destination) and (source in nodes) and (destination in nodes):
                probable_paths.extend(nx.all_shortest_paths(graph, source, destination))

    question_scores = {}
    for question_b in result_json_q["items"]:
        score = 0.0
        tag_count = 0.0
        for path in probable_paths:
            tags = questions_tags.get(question_b["question_id"])
            for tag in tags:
                if tag in path:
                    score = score + 1
                tag_count = tag_count + 1
        question_scores[question_b["question_id"]] = 0 if tag_count == 0 else score / tag_count
    print("Done.")
    print("Ranking answers based on comments...", end="")
    index = 0
    answer_scores = {}
    answers = {}
    for key in sorted(question_scores, key=question_scores.get):
        t_answer = get_answers_stackoverflow(key)
        for answer in t_answer["items"]:
            score = 0.0
            count = 0
            t_comments = get_comments_stackoverflow(key)
            for comment in t_comments["items"]:
                score = score + analyse_sentiment(comment)
                count = count + 1
            answer_scores[answer["answer_id"]] = 0 if count == 0 else score / count
            answers[answer["answer_id"]] = answer
            index = index + 1
            if index >= answer_limit:
                break
        if index >= answer_limit:
            break
    print("Done.")
    print("Answers found:")
    results = []
    for key in sorted(answer_scores, key=answer_scores.get):
        results.append((questions[answers[key]["question_id"]]["title"], answers[key]["body"]))

    return json.dumps(results)


question = input("Enter the search string:")
k = input("Enter number of answers:")
print(search(int(k), question))
