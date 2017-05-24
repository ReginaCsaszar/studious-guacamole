from flask import Flask, render_template, request, redirect
import data_manager
import datetime
app = Flask(__name__)


def vote_question_up(question_id):
    vote("question", "question.csv", "up", question_id, "question_id")
    return redirect("/question/{0}".format(question_id))


def vote_question_down(question_id):
    vote("question", "question.csv", "down", question_id, "question_id")
    return redirect("/question/{0}".format(question_id))


def vote_answer_up(question_id, answer_id):
    vote("answer", "answer.csv", "up", answer_id, "answer_id")
    return redirect("/question/{0}".format(question_id))


def vote_answer_down(question_id, answer_id):
    vote("answer", "answer.csv", "down", answer_id, "answer_id")
    return redirect("/question/{0}".format(question_id))


def vote(type_, filename, direction, id, key):
    query = "SELECT * FROM question WHERE id= '%'" % (id)
    data = data_manager.run_query(query)
    for row in data:
        if int(row[key]) == id:
            if direction == "up":
                row["vote_number"] = str(int(row["vote_number"]) + 1)
            else:
                row["vote_number"] = str(int(row["vote_number"]) - 1)
    data_manager.save_dict(data, type_, filename)


def displays_a_single_question(question_id):

    list_of_key_of_question = ["question_id", "submisson_time", "view_number", "vote_number", "title", "message"]
    title_of_question = ["ID", "Submisson time", "View number", "Vote number", "Title", "Message"]
    list_of_key_and_title_of_question = list(zip(list_of_key_of_question, title_of_question))

    list_of_key_of_answer = ["answer_id", "submisson_time", "vote_number", "question_id", "message"]
    title_of_answer = ["ID", "Submisson time", "Vote number", "Question id", "Message"]
    list_of_key_and_title_of_answers = list(zip(list_of_key_of_answer, title_of_answer))

    query = "SELECT * FROM question"
    rows = data_manager.run_query(query)
    list_of_names = ["question_id", "submisson_time", "view_number", "vote_number", "title", "message"]
    all_question = data_manager.build_dict(rows, list_of_names)
    for question_ in all_question:
        if question_id == question_["question_id"]:
            question = question_
            break

    query = "SELECT * FROM answer"
    rows = data_manager.run_query(query)
    list_of_names = ["answer_id", "submisson_time", "vote_number", "question_id", "message", "image"]
    all_answers = data_manager.build_dict(rows, list_of_names)
    answers = []
    for answer in all_answers:
        if question_id == answer["question_id"]:
            answers.append(answer)

    question_with_answers = {"question_id": question_id,
                             "question": question,
                             "answers": answers,
                             "list_of_key_of_question": list_of_key_of_question,
                             "list_of_key_of_answer": list_of_key_of_answer,
                             "title_of_question": title_of_question,
                             "title_of_answer": title_of_answer,
                             "list_of_key_and_title_of_question": list_of_key_and_title_of_question,
                             "list_of_key_and_title_of_answers": list_of_key_and_title_of_answers}

    return question_with_answers


def sort(data, sort_by, direction):
    try:
        sorted_data = sorted(data, key=lambda x: int(x[sort_by]), reverse=direction == "down")
    except:
        sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=direction == "down")

    return sorted_data

if __name__ == "__main__":
    app.run(debug=True)






