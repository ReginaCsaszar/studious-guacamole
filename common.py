import data_manager


def get_max_id(answers_list):
    """
    Return the the greatest id for answers.
    In case of empty list, return -1
    @answer_list: list of dictionaries (with answer_id key)
    """
    id_list = [int(answer["answer_id"]) for answer in answers_list]
    if len(id_list) == 0:
        return -1
    else:
        return max(id_list)


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


def get_index_from_id(list, id):
    """
    Return the index of an answer record by its id
    """
    for i in range(len(list)):
        if list[i]["answer_id"] == id:
            return i


def type_converter(dicts_in_list, keys, func):
    """
    This mapping function expects a list of dictionaries
    returns same data structure but func() is called on all key values with keys matching key param
    """
    for row in dicts_in_list:
        for key in row:
            if key in keys:
                row[key] = func(row[key])
    return dicts_in_list


def get_file_extension(string):
    dot_index = string[::-1].index('.')
    extension = string[::-1][:dot_index][::-1]
    return extension


def main():
    pass

if __name__ == '__main__':
    main()