from flask import Flask, request, render_template, redirect
import data_manager
import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/new-question')
def new_question():
    """Show new question page"""
    return render_template("new-question.html")


@app.route('/newpost', methods=["POST"])
def add_new_question():
    """Add new story to list, then redirect to /list page"""
    questions = data_manager.get_dict("question", "question.csv")
    row = {}
    row["question_id"] = str(len(questions))
    row["submisson_time"] = str(datetime.datetime.timestamp(datetime.datetime.now()))
    row["view_number"] = "0"
    row["vote_number"] = "0"
    row["title"] = request.form["title"]
    row["message"] = request.form["message"]
    row["image"] = request.form["image"]
    questions.append(row)
    data_manager.save_dict(questions, "question", "question.csv")
    return redirect("/list")


# @app.route("/question/<question_id>")

# @app.route("/question/<question_id>/new-answer")


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
