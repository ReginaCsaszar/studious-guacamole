from flask import Flask, request, render_template, redirect
import datetime
import data_manager
import common
app = Flask(__name__)

# @app.route("/")
# @app.route("/list")

# @app.route("/new-question")

# @app.route("/question/<question_id>")


@app.route("/question/<question_id>/new-answer", methods=["GET", "POST"])
def new_answer(question_id):
    if request.method == "POST":
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
    else:
        question = common.get_question(question_id)
        return render_template("answer.html", question=question)



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()