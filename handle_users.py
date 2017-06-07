from flask import Flask, request, render_template, redirect
import data_manager


def save_user_registration(username):
    table = users
    column_list = ['name']
    value_list = username
    data_manager.safe_insert(table, column_list, value_list)
    return redirect('/list')
