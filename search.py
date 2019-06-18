import json
import re

import networkx as nx
from flask import Flask
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, SentimentOptions
from stackapi import StackAPI

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


def get_questions_stackoverflow(query):
    """Fetches the questions from Stackoverflow API using the query provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("search/advanced", q=query, sort="relevance", accepted=True,
                      filter="withbody")
    return res


def get_answers_stackoverflow(question_ids):
    """Fetches the answers from Stackoverflow API using the question_id provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("questions/{ids}/answers", ids=question_ids, sort="votes", filter="withbody")
    return res


def get_comments_stackoverflow(answer_ids):
    """Fetches the comments from Stackoverflow API using the answer_id provided"""
    stack = StackAPI("stackoverflow")
    res = stack.fetch("answers/{ids}/comments", ids=answer_ids, sort="creation", filter="withbody")
    return res


def analyse_sentiment(sentence):
    """Calculates the compound index of the sentence using NLTK Vader SentimentAnalyser"""
    response = nlu.analyze(
        text=sentence,
        language="en",
        features=Features(sentiment=SentimentOptions())).get_result()
    return float(response["sentiment"]["document"]["score"])


@app.route("/<int:answer_limit>/<query>")
def search(answer_limit, query):
    question_tags = get_keywords(query)
    print("Extracted tags: ", end="")
    print(question_tags)
    result_json_q = get_questions_stackoverflow(space_separated_elements(question_tags))
    if len(result_json_q["items"]) < answer_limit:
        for i in range(0, len(question_tags) - 2):
            result_json_q["items"].extend(get_questions_stackoverflow(
                str(question_tags[i]) + " " + str(question_tags[i + 1]) + " " + str(question_tags[i + 2])))

    print("Got " + str(len(result_json_q["items"])) + " questions... processing.")
    questions_tags = {}
    edges = []
    nodes = []
    questions = {}
    if len(result_json_q["items"]) > 0:
        for question_b in result_json_q["items"]:
            if isinstance(question_b, dict):
                tags = list(set(get_keywords(question_b["title"])) | set(question_b["tags"]))
                questions_tags[question_b["question_id"]] = tags
                questions[question_b["question_id"]] = question_b
                questions[question_b["question_id"]]["answer_scores"] = {}
                for tag1 in tags:
                    if not (tag1 in nodes):
                        nodes.append(tag1)
                    for tag2 in tags:
                        if not (tag1 is tag2):
                            edges.append((tag1, tag2))
        print("Ranking questions... ")
        graph = nx.Graph()
        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)
        probable_paths = []
        for source in re.findall(r'\w+', query):
            for destination in question_tags:
                if not (source is destination) and (source in nodes) and (destination in nodes):
                    probable_paths.extend(nx.all_shortest_paths(graph, source, destination))
        question_scores = {}
        for question_b in questions.values():
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
        print("Ranking answers based on comments...")
        answers = {}
        questions_sorted = sorted(question_scores, key=question_scores.get, reverse=True)[:answer_limit]
        result_json_a = get_answers_stackoverflow(questions_sorted)
        for answer in result_json_a["items"]:
            answers[answer["answer_id"]] = answer
        result_json_c = get_comments_stackoverflow(answers.keys())
        comments = {}
        for comment in result_json_c["items"]:
            if comment["post_id"] in comments:
                comments[comment["post_id"]].append(comment)
            else:
                comments[comment["post_id"]] = [comment]

        for answer in answers.values():
            score = 0.0
            count = 0
            if answer["answer_id"] in comments.keys():
                t_comments = comments[answer["answer_id"]]
                for comment in t_comments:
                    score = score + analyse_sentiment(comment["body"])
                    count = count + 1
            questions[answer["question_id"]]["answer_scores"][answer["answer_id"]] = 0 if count == 0 else score / count

        print("Done.")
        print("Picking top answers for questions...")

        results = []
        index = 0
        for question_id in questions_sorted:
            question = questions[question_id]
            answer_id = max(question["answer_scores"], key=question["answer_scores"].get)
            results.append({"index": index, "question": question, "answer": answers[answer_id]})
            index = index + 1
        print("Done.")

        return json.dumps(results)


questionq = input("Enter the search string:")
k = input("Enter number of answers(max 50):")
print(search(50 if int(k) > 50 else int(k), questionq))
