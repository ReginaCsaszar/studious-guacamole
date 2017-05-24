from flask import Flask, request, render_template, redirect
import data_manager
import datetime


def new_question_route():
    """Show new question page"""
    title = "Add new question"
    action = "/newpost"
    data = {}
    return render_template("new-question.html", action=action, title=title, data=data)


def add_new_question():
    """Add new story to list, then redirect to /list page"""
    time = str(datetime.datetime.now())[:16]
    title = request.form["title"]
    message = request.form["message"]
    query = """INSERT INTO question (submission_time, view_number, vote_number, title, message) 
        VALUES ('{0}', 0, 0, '{1}', '{2}');""".format(time, title, message)
    data_manager.run_query(query)
    query = "SELECT id FROM question WHERE title='{0}';".format(title)
    question_id = data_manager.run_query(query)
    return redirect("/question/" + str(question_id[0][0]))


def edit_question_route(question_id):
    """Find question details from id and redirect with the data to /new_question page"""
    title = "Modify question"
    action = "/modify/" + question_id
    query = "SELECT title, message FROM question WHERE id = '{0}';".format(question_id)
    table = data_manager.run_query(query)
    titles = "title", "message",
    data = data_manager.build_dict(table, titles)[0]
    return render_template("new-question.html", title=title, data=data, action=action)


def edit_question(question_id):
    """Update question in the database, then go back to question's page"""
    title = request.form["title"]
    message = request.form["message"]
    print(title, message, question_id)
    query = "UPDATE question SET title = '{0}', message = '{1}' WHERE id = '{2}';".format(title, message, question_id)
    data_manager.run_query(query)
    return redirect("/question/"+question_id)


def delete_question(question_id):
    """ Delete question from database then redirect to /list page"""
    query = "DELETE FROM question WHERE id = '{0}';".format(question_id)
    data_manager.run_query(query)
    return redirect("/list")


def main():
    pass

if __name__ == '__main__':
    main()
