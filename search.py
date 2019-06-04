import json


def get_statement():
    """Fetches the problem statement by user input"""
    # TODO: return the problem statement by taking input from the user
    return "Keyword extraction using NLTK from a sentence"


def get_keywords(sentence):
    """Fetches the keywords of the given sentence"""
    # TODO: detect the keywords using NLTK, and corpus stopwords, from the sentence and return the array of keywords
    return ["keyword", "extraction", "nltk", "sentence"]


def space_separated_elements(array):
    """Converts the question_tags array to a space separated string"""
    # TODO: return a string containing all the elements of the array, separated by a space
    return "keyword extraction nltk sentence"


def get_questions_stackoverflow(query):
    """Fetches the questions from Stackoverflow API using the query provided"""
    # TODO: get the relevant questions from Stackoverflow API search by using query as q and sort by activity,
    #  in descending order and return the response as json object (dict)
    return json.loads(
        '{"items":[{"tags":["python","nlp","nltk"],"owner":{"reputation":1825,"user_id":436441,"user_type":"registered","accept_rate":80,"profile_image":"https://i.stack.imgur.com/g4GtM.jpg?s=128&g=1","display_name":"waigani","link":"https://stackoverflow.com/users/436441/waigani"},"is_answered":true,"view_count":11892,"answer_count":3,"score":5,"last_activity_date":1540208156,"creation_date":1341894786,"last_edit_date":1341896827,"question_id":11406657,"link":"https://stackoverflow.com/questions/11406657/python-nltk-keyword-extraction-from-sentence","title":"python nltk keyword extraction from sentence"},{"tags":["python","algorithm","machine-learning","nlp"],"owner":{"reputation":98,"user_id":1684021,"user_type":"registered","accept_rate":0,"profile_image":"https://www.gravatar.com/avatar/c32dd263478a6fc8ce85452348b27cd2?s=128&d=identicon&r=PG","display_name":"Coeus2016","link":"https://stackoverflow.com/users/1684021/coeus2016"},"is_answered":true,"view_count":2873,"answer_count":1,"score":4,"last_activity_date":1460498288,"creation_date":1460320212,"last_edit_date":1460483248,"question_id":36535206,"link":"https://stackoverflow.com/questions/36535206/name-entity-resolution-algorithm","title":"Name Entity Resolution Algorithm"},{"tags":["python","nlp","nltk","tf-idf"],"owner":{"reputation":1825,"user_id":436441,"user_type":"registered","accept_rate":80,"profile_image":"https://i.stack.imgur.com/g4GtM.jpg?s=128&g=1","display_name":"waigani","link":"https://stackoverflow.com/users/436441/waigani"},"is_answered":true,"view_count":1526,"accepted_answer_id":11550101,"answer_count":1,"score":1,"last_activity_date":1342728786,"creation_date":1342553051,"last_edit_date":1495542473,"question_id":11529424,"link":"https://stackoverflow.com/questions/11529424/implementing-idf-with-nltk","title":"Implementing idf with nltk"}],"has_more":false,"quota_max":300,"quota_remaining":270}')


def get_all_paths(nodes, edges, source, destination):
    """Finds the possible paths between the source and destination nodes, in the graph depicted by nodes and edges."""
    # TODO: find the paths possible between two nodes and return as list of list of traversed nodes
    return []


def keys_sorted_by_value(dictionary):
    """Sorts the dictionary in descending order of values and returns an array containing keys"""
    # TODO: return an array containing the keys of the dictionary sorted by the value corresponding
    #  to the key in descending order
    return []


def get_answers_stackoverflow(question_id):
    """Fetches the answers from Stackoverflow API using the question_id provided"""
    # TODO: get the answers from Stackoverflow API by using the provided question_id and sort by rating,
    #  in descending order and return the response as json object (dict)
    return json.loads("{}")


def get_comments_stackoverflow(question_id):
    """Fetches the comments from Stackoverflow API using the answer_id provided"""
    # TODO: get the comments from Stackoverflow API by using the provided answer_id
    # and return the response as json object (dict)
    return json.loads("{}")


def analyse_compound_sentiment(sentence):
    """Calculates the compound index of the sentence using NLTK Vader SentimentAnalyser"""
    # TODO: returns the compound index of sentiment analysis over the statement using NLTK Vader
    return 0.5


question = input("Enter the problem statement: ")
question_tags = get_keywords(question)
query = space_separated_elements(question_tags)
result_json_q = get_questions_stackoverflow(query)
if "items" in result_json_q:
    questions_tags = {}
    edges = []
    nodes = []
    for question_b in result_json_q["items"]:
        tags = question_b["tags"]
        """if "body" in question_b:
            tags = get_keywords(question_b["body"])
        elif "tags" in question_b:
            tags= question_b["tags"]
        else:
            tags = get_keywords(question_b["title"])"""
        questions_tags[question_b["question_id"]] = tags
        for tag1 in tags:
            if not (tag1 in nodes):
                nodes.append(tag1)
            for tag2 in tags:
                if not (tag1 is tag2):
                    edges.append((tag1, tag2))
    print(edges)
    print(nodes)
    probable_paths = []
    for source in question_tags:
        for destination in question_tags:
            if not (source is destination) and (source in nodes) and (destination in nodes):
                paths = get_all_paths(nodes, edges, source, destination)
                for path in paths:
                    flag = True
                    for tag in question_tags:
                        if (not (source is tag)) and (not (destination is tag)):
                            flag = flag and tag in path
                    if flag:
                        probable_paths.append(path)
    question_scores = {}
    for question_b in result_json_q["items"]:
        score = 0
        for path in probable_paths:
            tags = questions_tags.get(question_b["question_id"])
            for tag in tags:
                if tag in path:
                    score = score + 1
        question_scores[question_b["question_id"]] = score

    k = input("Enter the number of answers (k): ")
    index = 0
    answer_scores = {}
    answer_bodies = {}
    for key in keys_sorted_by_value(question_scores):
        t_answer = get_answers_stackoverflow(key)
        for answer in t_answer["items"]:
            score = 0.0
            count = 0
            t_comments = get_comments_stackoverflow(key)
            for comment in t_comments["items"]:
                score = score + analyse_compound_sentiment(comment)
                count = count + 1
            answer_scores[answer["answer_id"]] = score / count
            answer_bodies[answer["answer_id"]] = answer["body"]
            index = index + 1
            if index >= k:
                break
        if index >= k:
            break
    index = 1
    for key in keys_sorted_by_value(answer_scores):
        print index + "." + answer_bodies[key] + "\n"
        index = index + 1
