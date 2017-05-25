"""Search in questions & answers module
"""

from flask import Flask, request, render_template, redirect
import data_manager


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
    return render_template('search_results.html', questions=questions)


def main():
    pass


if __name__ == '__main__':
    main()
