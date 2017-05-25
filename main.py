import datetime
import data_manager
import common
import displays_a_question
import listpage
import handle_question
from flask import Flask, request, render_template, redirect
from displays_a_question import sort
from displays_a_question import vote

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/list")


@app.route('/extendurl/<col_idx>')
def extend_url(col_idx):
    return listpage.extend_url(col_idx)


@app.route("/list")
def print_table():
    return listpage.print_table()


@app.route('/new-question')
def new_question():
    """Show new question page"""
    return handle_question.new_question_route()


@app.route('/newpost', methods=["POST"])
def add_new_question():
    """Add new story to list, then redirect to /list page"""
    return handle_question.add_new_question()


@app.route('/question/<question_id>/edit')
def edit_question_route(question_id):
    return handle_question.edit_question_route(question_id)


@app.route('/modify/<question_id>', methods=["POST"])
def edit_question(question_id):
    return handle_question.edit_question(question_id)


@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    return handle_question.delete_question(question_id)


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


@app.route("/question/<int:question_id>")
def displays_a_single_question_A(question_id):
    question_with_answers = displays_a_question.displays_a_single_question(question_id)
    sort_by = request.args.get("sort_by", "answer_id")
    direction = request.args.get("direction", "up")
    question_with_answers["sort_by"] = sort_by
    question_with_answers["direction"] = direction
    return render_template("display_a_question.html", question_with_answers=question_with_answers)


# v2.0
@app.route("/answer/<answer_id>/edit")
def edit_answer(answer_id):
    answer = common.get_answer(answer_id)
    question = common.get_question(answer["question_id"])
    return render_template("answer.html", question=question, answer=answer, mode="Edit", error="")


# v2.0
@app.route("/answer/<answer_id>/edit", methods=["POST"])
def edit_answer_post(answer_id):
    if len(request.form["answer"]) < 10:
        answer = common.get_answer(answer_id)
        question = common.get_question(answer["question_id"])
        return render_template("answer.html", question=question, answer=answer, mode="Edit", error="10 char")
    answer = common.get_answer(answer_id)
    answer["message"] = request.form["answer"]
    common.update("answer", answer_id, "message", answer["message"])
    return redirect("/question/{}".format(answer["question_id"]), code=302)

# v2.0
@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    answer = common.get_answer(answer_id)
    question = common.get_question(answer["question_id"])
    date_time = answer["submission_time"]
    return render_template("del_answer.html", answer=answer, question=question, date_time=date_time)


@app.route("/answer/<answer_id>/delete", methods=["POST"])
def delete_answer_post(answer_id):
        answer = common.get_answer(answer_id)
        common.delete("answer", answer_id)
        return redirect("/question/{}".format(answer["question_id"]), code=302)


@app.route("/question/<question_id>/new-answer")
def new_answer(question_id):
    question = common.get_question(question_id)
    return render_template("answer.html", question=question, mode="Send new", error="")


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def new_answer_post(question_id):
    if len(request.form["answer"]) < 10:
        question = common.get_question(question_id)
        return render_template("answer.html", question=question, mode="Send new", error="")
    answers_list = data_manager.get_dict("answer", "answer.csv")
    answer = {}
    answer["answer_id"] = str(common.get_max_id(answers_list) + 1)
    answer["submisson_time"] = str(datetime.datetime.timestamp(datetime.datetime.now()))
    answer["vote_number"] = "0"
    answer["question_id"] = question_id
    answer["message"] = request.form["answer"]
    answer["image"] = ""
    answers_list.append(answer)
    data_manager.save_dict(answers_list, "answer", "answer.csv")
    return redirect("/", code=302)


@app.route('/question/<question_id>/new-comment')
def add_new_question_comment(question_id):
    return handle_comments.add_new_question_comment(question_id)


@app.route('/answer/<answer_id>/new-comment')
def add_new_answer_comment(answer_id):
    return handle_comments.add_new_answer_comment(answer_id)


@app.route('/comments/<comment_id>/edit')
def edit_comment(comment_id):
    return handle_comments.edit_comment(comment_id)


@app.route('/comments/<comment_id>/delete')
def delete_comment(comment_id):
    return handle_comments.delete_comment(comment_id)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
