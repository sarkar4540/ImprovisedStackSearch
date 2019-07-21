from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import re
from datetime import timedelta
from functools import update_wrapper

import networkx as nx
import nltk
from flask import Flask, make_response, request, current_app
from future import standard_library
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, SentimentOptions
from stackapi import StackAPI

app = Flask(__name__, static_url_path='', static_folder='frontend')

standard_library.install_aliases()

stack = StackAPI("stackoverflow")

nlu = NaturalLanguageUnderstandingV1(
    iam_apikey="1A3R_SmipU_wkdOjJRwSxZPmn6dIgriROn4M6zngTR3v", version="2018-11-16",
    url="https://gateway-lon.watsonplatform.net/natural-language-understanding/api")


def get_keywords(sentence):
    """Fetches the keywords of the given sentence using IBM Watson Natural Language Understanding API"""
    keywords = []
    response = nlu.analyze(
        text=sentence,
        language="en",
        features=Features(keywords=KeywordsOptions())).get_result()
    for keyword_obj in response['keywords']:
        keywords.append(keyword_obj["text"].lower())
    return separate_elements(keywords)


def space_separated_elements(array):
    """Converts the question_tags array to a space delimited string."""
    string = ""
    for element in array:
        string = string + element + " "

    return string


def separate_elements(array):
    """splits the strings, delimited by whitespace in the provided list and adds each newly formed string
    to the returned list"""
    list_a = []
    for element in array:
        list_a.extend(element.split(" "))
    return list_a


def get_questions_stackoverflow(query):
    """Fetches the questions from StackAPI using the query provided"""
    stack.page_size = 50
    stack.max_pages = 1
    res = stack.fetch("search/advanced", q=query, sort="relevance", accepted=True,
                      filter="withbody")
    return res


def get_answers_stackoverflow(question_ids):
    """Fetches the answers from StackAPI corresponding the question_ids provided"""
    stack.page_size = 100
    stack.max_pages = 1
    res = stack.fetch("questions/{ids}/answers", ids=question_ids, sort="votes", filter="withbody")
    return res


def get_comments_stackoverflow(answer_ids):
    """Fetches the comments from StackAPI corresponding to the answer_ids provided"""
    stack.page_size = 100
    stack.max_pages = 1
    res = stack.fetch("answers/{ids}/comments", ids=answer_ids, sort="creation", filter="withbody")
    return res


def analyse_sentiment(sentence):
    """Calculates the compound index of the sentence using IBM Watson Natural Language Understanding API"""
    response = nlu.analyze(
        text=sentence,
        language="en",
        features=Features(sentiment=SentimentOptions())).get_result()
    return float(response["sentiment"]["document"]["score"])


def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    """Allows cross domain access of the Flask route decorated with this decorator"""
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


@app.route("/")
@crossdomain(origin='*')
def root():
    """Method invoked for the root route of the Web Application"""
    return app.send_static_file('index.html')


@app.route("/api/<query>/<answer_limit>")
@crossdomain(origin='*')
def searchw(query=None, answer_limit=50):
    """Method invoked for the api route of the Web application"""
    return search(query, answer_limit)


def search(query=None, answer_limit=50):
    """Searches StackOverflow for solutions corresponding to query, limited by answer_limit. Returns a list
    of elements containing index, question and answer."""
    answer_limit = int(answer_limit)
    if query is None:
        return json.dumps({"error": "Enter a query to search."})
    question_tags = get_keywords(query)
    print("Extracted tags: ", end="")
    print(question_tags)
    result_json_q = get_questions_stackoverflow(space_separated_elements(question_tags))
    if len(result_json_q["items"]) < answer_limit:
        for i in range(0, len(question_tags) - 2):
            result_json_q["items"].extend(get_questions_stackoverflow(
                str(question_tags[i]) + " " + str(question_tags[i + 1]) + " " + str(question_tags[i + 2]))["items"])

    print("Got " + str(len(result_json_q["items"])) + " questions... processing.")
    questions_tags = {}
    edges = []
    nodes = []
    questions = {}
    if len(result_json_q["items"]) > 0:
        for question_b in result_json_q["items"]:
            if isinstance(question_b, dict):
                tags = list(set(get_keywords(question_b["title"])) | set(question_b["tags"]))
                questions_tags[int(question_b["question_id"])] = tags
                questions[int(question_b["question_id"])] = question_b
                questions[int(question_b["question_id"])]["answer_scores"] = {}
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
                tags = questions_tags[int(question_b["question_id"])]
                for tag in tags:
                    if tag in path:
                        score = score + 1
                    tag_count = tag_count + 1
            distance = nltk.edit_distance(query, question_b['title'])
            question_scores[int(question_b["question_id"])] = (((1.0 / distance) if distance != 0 else 1) + (
                0 if tag_count == 0 else score / tag_count)) / 2

        answers = {}
        questions_sorted = sorted(question_scores, key=lambda ind: int(question_scores.get(ind) * 10000), reverse=True)[
                           :answer_limit]
        print("Done.")
        print("Fetching and ranking answers based on comments...")
        result_json_a = get_answers_stackoverflow(questions_sorted)
        max_score = 1
        for answer in result_json_a["items"]:
            answers[int(answer["answer_id"])] = answer
            ascore = int(answer["score"])
            if ascore > max_score:
                max_score = ascore

        result_json_c = get_comments_stackoverflow(answers.keys())
        comments = {}
        for comment in result_json_c["items"]:
            if comment["post_id"] in comments:
                comments[int(comment["post_id"])].append(comment)
            else:
                comments[int(comment["post_id"])] = [comment]

        for answer in answers.values():
            score = 0.0
            count = 1
            a_score = int(answer["score"])
            accepted = bool(answer["is_accepted"])
            if int(answer["answer_id"]) in comments.keys():
                t_comments = comments[int(answer["answer_id"])]
                for comment in t_comments:
                    score = score + analyse_sentiment(comment["body"])
                    count = count + 1
            questions[int(answer["question_id"])]["answer_scores"][
                int(answer["answer_id"])] = (a_score / max_score + score / count + (
                0.5 if accepted else 0)) / 3

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


port = int(os.getenv('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
