from flask import Flask, request, render_template, redirect
import datetime
import data_manager
import common

app = Flask(__name__)

@app.route("/")
def index():
    return 'HOMEPAGE'


@app.route('/extend/<idx>')
def extend_url(idx):
    order = {key: request.args[key] for key in request.args}
    if idx not in order:
        order[idx] = 'desc'
    elif order[idx] == 'desc':
        order[idx] = 'asc'
    else:
        order.pop(idx)
    url = '&'.join([key + '=' + order[key] for key in order])
    url = '/list?' + url
    print(url)
    return redirect(url)


@app.route("/list")
def print_table():
    pairs = {'ID': 'question_id', 'Question': 'title', 'Date': 'submisson_time', 'Number of Views': 'view_number','Votes': 'vote_number'}
    questions = data_manager.get_dict('question', 'question.csv')
    order = request.args
    for key in order.keys():
        questions = sorted(questions, key=lambda x: x[pairs[key]], reverse=True if order[key] == 'desc' else False)
    url = '&'.join([key + '=' + order[key] for key in order])
    return render_template('list.html', questions=questions, url=url)






def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()