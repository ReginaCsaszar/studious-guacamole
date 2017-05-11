import datetime
import data_manager
import common
import displays_a_question
import listpage
from flask import request, render_template, redirect


def extend_url(idx):
    """
    Extends the query string in the Url with the latest sorting priority input
    """
    order = {key: request.args[key] for key in request.args}
    if idx not in order:
        order[idx] = 'desc'
    elif order[idx] == 'desc':
        order[idx] = 'asc'
    else:
        order.pop(idx)
    url = '&'.join([key + '=' + order[key] for key in order])
    url = '/list?' + url
    return redirect(url)


def print_table():
    """
    Based on sorting priorities stored in the query string,
    lists Questions with list.html
    """
    pairs = {
        'ID': 'question_id', 'Question': 'title', 'Date': 'submisson_time',
        'Number of Views': 'view_number', 'Votes': 'vote_number'
        }
    numeric_atr = ['question_id', 'submisson_time', 'view_number', 'vote_number']
    questions = data_manager.get_dict('question', 'question.csv')
    questions = common.type_converter(questions, numeric_atr, lambda x: int(float(x)))
    order = request.args
    for key in order.keys():
        questions = sorted(questions, key=lambda x: x[pairs[key]], reverse=True if order[key] == 'desc' else False)
    questions = common.type_converter(questions, ['submisson_time'], lambda x: datetime.date.fromtimestamp(x))
    url = '&'.join([key + '=' + order[key] for key in order])
    return render_template('list.html', questions=questions, url=url)
