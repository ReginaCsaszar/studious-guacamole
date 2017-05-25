import data_manager
from flask import FLASK, render_template


def add_new_question_comment(question_id):
    sql_query = """SELECT message FROM question WHERE id='question_id'"""
    question_content = data_manager.run_query(sql_query)[0][0]
    return render_template(
        'comment.html', basis='question', mode='Add_new',
        content=question_content, id='question_id', title='Add a'
        )


def add_new_answer_comment(answer_id):
    return handle_comments.add_new_answer_comment(answer_id)


def edit_comment(comment_id):
    return handle_comments.edit_comment(comment_id)


def delete_comment(comment_id):
    return handle_comments.delete_comment(comment_id)