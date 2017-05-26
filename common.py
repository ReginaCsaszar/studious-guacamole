import data_manager


def get_comments(comment_type, question_id):
    if comment_type == "question":
        query = """SELECT * 
                FROM comment
                WHERE question_id = {};
                """.format(question_id)
    elif comment_type == "answer":
        query = """SELECT comment.id, comment.question_id, comment.answer_id, comment.message, comment.submission_time, comment.edited_count
                FROM comment
                LEFT JOIN answer ON answer_id = answer.id
                WHERE answer.question_id = {};
                """.format(question_id)
    rows = data_manager.run_query(query)
    columns = ["id", "question_id", "answer_id", "message", "submission_time", "edited_count"]
    comments = data_manager.build_dict(rows, columns)
    return comments


def get_question(id):
    """
    Return a single question (dict) by its ID
    """
    question = data_manager.run_query("SELECT * FROM question WHERE id={};".format(id))
    question = data_manager.build_dict(question, ["question_id", "submission_time", "view_number", "vote_number", "title", "message", "image"])
    return question[0]


def get_answer(id):
    """
    Return a single answer (dict) by its ID
    """
    answer = data_manager.run_query("SELECT * FROM answer WHERE id={};".format(id))
    answer = data_manager.build_dict(answer, ["answer_id", "submission_time", "vote_number", "question_id", "message", "image"])
    return answer[0]


def update(table, id, column, value):
    """
    Build an update sql query in the format:
    UPDATE {table} SET {column}='{value}' WHERE id='{id}';
    and call it.
    """
    query = "UPDATE {0} SET {1}='{2}' WHERE id='{3}';".format(table, column, value, id)
    data_manager.run_query(query)
    return


def delete(table, id):
    """
    Build a delete sql query in the format:
    DELETE FROM {table} WHERE id={id};
    and call it.
    """
    query = "DELETE FROM {0} WHERE id={1};".format(table, id)
    data_manager.run_query(query)
    return


def insert_answer(record):
    """
    Build an insert into sql query in the format:
    INSERT INTO answer (vote_number, question_id, message) VALUES ({values});
    @record: dictionary keys = column name, values = values
    """
    columns = ["vote_number", "question_id", "message", "submission_time"]
    values = [record["vote_number"], record["question_id"], record["message"], record["submission_time"]]
    data_manager.safe_insert("answer", columns, values)
    return


def get_file_extension(string):
    dot_index = string[::-1].index('.')
    extension = string[::-1][:dot_index][::-1]
    return extension
