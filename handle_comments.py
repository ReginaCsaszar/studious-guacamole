import datetime
import data_manager
from flask import Flask, render_template, redirect


def add_new_question_comment(question_id):
    sql_query = """SELECT message FROM question WHERE id={}""".format(question_id)
    question_content = data_manager.run_query(sql_query)[0][0]
    return render_template(
        'comment.html', basis='question', mode='Add_new', button='Create',
        content=question_content, question_id=str(question_id), answer_id='', title='Add a'
        )


def add_comment_to_db(q_or_a, id, comment):
    curr_time = str(datetime.datetime.now())[:16]
    if q_or_a == 'question':
        print(id, comment, curr_time)
        sql_query = (
            """INSERT INTO comment (question_id, message, submission_time)
            VALUES ({}, '{}', '{}');""".format(id, comment, curr_time)
        )
        question_id = id
    else:
        sql_query = (
            """INSERT INTO comment (answer_id, message, submission_time, edited_number)
            VALUES ({}, {}, {}, 0 )""".format(id, comment, curr_time)
        )
        question_id = data_manager.run_query("""SELECT question_id FROM answer WHERE id={}""".format(id))
    data_manager.run_query(sql_query)
    return redirect('/question/' + question_id)

def add_new_answer_comment(answer_id):
    return handle_comments.add_new_answer_comment(answer_id)



def edit_comment(comment_id):
    return handle_comments.edit_comment(comment_id)


def delete_comment(comment_id):
    return handle_comments.delete_comment(comment_id)