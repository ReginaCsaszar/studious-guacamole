from flask import Flask, request, render_template, redirect
import datetime
import data_manager
import common
app = Flask(__name__)

# @app.route("/")
# @app.route("/list")

# @app.route("/new-question")

# @app.route("/question/<question_id>")


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    answer = common.get_answer(answer_id)
    question = common.get_question(answer["question_id"])
    date_time = datetime.datetime.fromtimestamp(int(float(answer["submisson_time"]))).strftime('%Y-%m-%d %H:%M:%S')
    return render_template("del_answer.html", answer=answer, question=question, date_time=date_time)


@app.route("/answer/<answer_id>/delete", methods=["POST"])
def delete_answer_post(answer_id):
    return "Mindent törölni!!"


@app.route("/question/<question_id>/new-answer")
def new_answer(question_id):
    question = common.get_question(question_id)
    return render_template("answer.html", question=question, error="")


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def new_answer_post(question_id):
    if len(request.form["answer"]) < 10:
        question = common.get_question(question_id)
        return render_template("answer.html", question=question, error="10 char")
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


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()