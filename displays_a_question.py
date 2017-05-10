from flask import Flask, render_template, request, redirect
import data_manager
app = Flask(__name__)


@app.route("/question/<int:question_id>/vote-up")
def vote_question_up(question_id):
    vote("question", "question.csv", "up", question_id, "question_id")
    return redirect("/question/{0}".format(question_id))


@app.route("/question/<int:question_id>/vote-down")
def vote_question_down(question_id):
    vote("question", "question.csv", "down", question_id, "question_id")
    return redirect("/question/{0}".format(question_id))


@app.route("/question/<int:question_id>/<int:answer_id>/vote-up")
def vote_answer_up(question_id, answer_id):
    vote("answer", "answer.csv", "up", answer_id, "answer_id")
    return redirect("/question/{0}".format(question_id))


@app.route("/question/<int:question_id>/<int:answer_id>/vote-down")
def vote_answer_down(question_id, answer_id):
    vote("answer", "answer.csv", "down", answer_id, "answer_id")
    return redirect("/question/{0}".format(question_id))


def vote(type_, filename, direction, id, key):
    data = data_manager.get_dict(type_, filename)
    for row in data:
        if int(row[key]) == id:
            if direction == "up":
                row["vote_number"] = str(int(row["vote_number"]) + 1)
            else:
                row["vote_number"] = str(int(row["vote_number"]) - 1)
    data_manager.save_dict(data, type_, filename)


@app.route("/question/<int:question_id>")
def displays_a_single_question(question_id):

    list_of_key_of_question = ["question_id", "submisson_time", "view_number", "vote_number", "title", "message", "image"]
    title_of_question = ["ID", "Submisson time", "View number", "Vote number", "Title", "Message", "Image"]
    list_of_key_and_title_of_question = list(zip(list_of_key_of_question, title_of_question))

    list_of_key_of_answer = ["answer_id", "submisson_time", "vote_number", "question_id", "message", "image"]
    title_of_answer = ["ID", "Submisson time", "Vote number", "Question id", "Message", "Image"]
    list_of_key_and_title_of_answers = list(zip(list_of_key_of_answer, title_of_answer))

    data_question = data_manager.get_dict("question", "question.csv")
    question = {}
    for row in data_question:
        if int(row["question_id"]) == question_id:
            for index, name in enumerate(list_of_key_of_question):
                question[name] = row[name]
            break

    data_answers = data_manager.get_dict("answer", "answer.csv")
    answers = []
    for row in data_answers:
        answer = {}
        if int(row["question_id"]) == question_id:
            for index, name in enumerate(list_of_key_of_answer):
                answer[name] = row[name]
        answers.append(answer)

    sort_by = request.args.get("sort_by", "answer_id")
    direction = request.args.get("direction", "up")
    answers = sort(answers, sort_by, direction)
    question_with_answers = {"question_id": question_id,
                             "question": question,
                             "answers": answers,
                             "list_of_key_of_question": list_of_key_of_question,
                             "list_of_key_of_answer": list_of_key_of_answer,
                             "title_of_question": title_of_question,
                             "title_of_answer": title_of_answer,
                             "list_of_key_and_title_of_question": list_of_key_and_title_of_question,
                             "list_of_key_and_title_of_answers": list_of_key_and_title_of_answers}

    return render_template("display_a_question.html", question_with_answers=question_with_answers)


def sort(data, sort_by, direction):
    try:
        sorted_data = sorted(data, key=lambda x: int(x[sort_by]), reverse=direction == "down")
    except:
        sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=direction == "down")

    return sorted_data

if __name__ == "__main__":
    app.run(debug=True)
 




