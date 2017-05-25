"""As a user I want to search in questions & answers.
There should be a search box on the main page and a button.
If I write something in the search box and press the button:
I want to see a list of all questions (same data as in the list page):
 - which title contains the text in the search box or
 - which have answers which message contains the text in the search box.
(/search?q=<search phrase>
"""

from flask import Flask, request, render_template, redirect
import data_manager


# @app.route('/search?q=<search phrase>')
def search_questions(term):
    answer_query = """SELECT question_id FROM answer
                   WHERE message LIKE '%{0}%' ;""".format(term)
    ids = data_manager.run_query(answer_query)
    filters = ""
    for elem in set(ids):
        filters = filters + " OR id=" + str(elem[0])
    question_query = """SELECT id, title, submission_time, view_number, vote_number FROM question WHERE title LIKE '%{0}%'{1};""".format(term, filters)
    table = data_manager.run_query(question_query)
    keys = ("question_id", "title", "submission_time", "view_number", "vote_number")
    questions = data_manager.build_dict(table, keys)
    return render_template('list.html', questions=questions, url="")


def main():
    print(search_questions("e"))
    pass

if __name__ == '__main__':
    main()
