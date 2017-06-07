from flask import Flask, request, render_template, redirect
import data_manager


def save_user_registration(username):
    table = 'users'
    column_list = ['name']
    value_list = (username,)
    data_manager.safe_insert(table, column_list, value_list)
    return redirect('/list')


def list_users():
    sql_query = """SELECT u.name, u.submission_time, COUNT(q.users_id), COUNT(a.users_id)
    FROM ((users u LEFT OUTER JOIN question q
    ON (u.id = q.users_id))
        LEFT OUTER JOIN answer a
        ON (u.id = a.users_id))
    GROUP BY u.id
    ORDER BY u.submission_time;"""
    header = ('Username', 'Join Date', 'Number of Questions', 'Number of Answers')
    table = data_manager.run_query(sql_query)
    return render_template('print_users.html', title='List of Users', table=table, header=header)
