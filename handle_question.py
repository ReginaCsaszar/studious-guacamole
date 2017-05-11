from flask import Flask, request, render_template, redirect
import data_manager
import datetime


def new_question_route():
    """Show new question page"""
    title = "Add new question"
    action = "/newpost"
    return render_template("new-question.html", action=action, title=title)


def add_new_question():
    """Add new story to list, then redirect to /list page"""
    questions = data_manager.get_dict("question", "question.csv")
    row = {}
    ident = len(questions)
    row["question_id"] = str(ident)
    row["submisson_time"] = str(datetime.datetime.timestamp(datetime.datetime.now()))
    row["view_number"] = "0"
    row["vote_number"] = "0"
    row["title"] = request.form["title"]
    row["message"] = request.form["message"]
    row["image"] = ""
    questions.append(row)
    data_manager.save_dict(questions, "question", "question.csv")
    return redirect("/question/<ident>")


def edit_question_route(question_id):
    title = "Modify question"
    action = "/modify/" + question_id
    data = data_manager.question_id(question_id)
    return render_template("new-question.html", title=title, data=data)


def edit_question(question_id):
    questions = data_manager.get_dict("question", "question.csv")
    for question in questions:
        if question["question_id"] == question_id:
            question["title"] = request.form["title"]
            question["message"] = request.form["message"]
            break
    data_manager.save_dict(questions, "question", "question.csv")
    ident = int(question_id)
    return redirect("/question/<ident>")


@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    questions = data_manager.get_dict("question", "question.csv")
    updated_questions = [row for row in questions if row["question_id"] != question_id]
    answers = data_manager.get_dict("answer", "answer.csv")
    updated_answers = [row for row in questions if row["question_id"] != question_id]
    return redirect("/list")


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
