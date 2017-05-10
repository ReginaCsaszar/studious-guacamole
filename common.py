import data_manager


def get_max_id(answers_list):
    id_list = [int(answer["answer_id"]) for answer in answers_list]
    return max(id_list)


def get_question(id):
    questions_list = data_manager.get_dict("question", "question.csv")
    for question in questions_list:
        if question["question_id"] == id:
            return question


def main():
    pass

if __name__ == '__main__':
    main()