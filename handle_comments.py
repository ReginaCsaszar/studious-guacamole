import datetime
import data_manager
from flask import FLASK, render_template


def add_new_question_comment(question_id):
    sql_query = """SELECT message FROM question WHERE id='question_id'"""
    question_content = data_manager.run_query(sql_query)[0][0]
    return render_template(
        'comment.html', basis='question', mode='Add_new', button='Create'
        content=question_content, question_id='question_id', answer_id='', title='Add a'
        )


def add_comment_to_db(question_id, answer_id, comment):
    curr_time = str(datetime.datetime.now())[:16]
    sql_query = (
        """INSERT INTO comment (question_id, answer_id, message, submission_time, edited_number)
        VALUES ({}, is NULL, {}, {}, 0 )""".format(question_id, comment, curr_time)
    )
    data_manager.run_query(sql_query)
    return redirect('/question/' + question_id)

def add_new_answer_comment(answer_id):
    return handle_comments.add_new_answer_comment(answer_id)



def edit_comment(comment_id):
    return handle_comments.edit_comment(comment_id)


def delete_comment(comment_id):
    return handle_comments.delete_comment(comment_id)