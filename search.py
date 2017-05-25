"""Search in questions & answers module
"""

from flask import Flask, request, render_template, redirect
import data_manager


def make_query_conditions(items):
    """create a condition for query from given list"""
    result = ""
    for elem in set(items):
        result = result + " OR id=" + str(elem[0])
    return result


def make_fancy(term, table, key):
    """insert html tag into string for jinja formatting"""
    new = "<mark>" + term + "</mark>"
    for row in table:
        row[key] = row[key].replace(term, new)
    return table


def search_questions(term):
    """search for answers and questions with the given search term and display it"""
    # search for answers with search term in their message
    answer_query = """SELECT question_id FROM answer
                   WHERE message LIKE '%{0}%' ;""".format(term)
    ids = data_manager.run_query(answer_query)
    filters = make_query_conditions(ids)
    # slect questions with search term in their title and for those which id given by previous answers
    question_query = """SELECT id, title, message, submission_time FROM question WHERE title LIKE '%{0}%'{1};""".format(term, filters)
    table = data_manager.run_query(question_query)
    if table:
        keys = ("question_id", "title", "message", "submission_time")
        questions = data_manager.build_dict(table, keys)
        fancy_questions = make_fancy(term, questions, "title")
    else:
        return render_template('search_results.html', questions=[], answers=[])
    # select related answers
    ids = []
    for row in questions:
        ids.append(str(row["question_id"]))
    filters = make_query_conditions(ids)[4:]
    answer_query = """SELECT id, message, question_id FROM answer WHERE {0};""".format(filters)
    table = data_manager.run_query(answer_query)
    keys = ("answer_id", "message", "question_id")
    answers = data_manager.build_dict(table, keys)
    fancy_answers = make_fancy(term, answers, "message")
    return render_template('search_results.html', questions=fancy_questions, answers=fancy_answers)


def main():
    pass


if __name__ == '__main__':
    main()
