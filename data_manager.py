"""Data manager functions"""
import os


current_file_path = os.path.dirname(os.path.abspath(__file__))+"/data/"


def get_table_from_file(filename):
    """Read data from file
    """
    with open(current_file_path+filename, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    return table


def write_table_to_file(table, filename):
    """Write data to file
    """
    with open(current_file_path+filename, "w") as file:
        for record in table:
            row = ','.join(record)
            file.write(row + "\n")


def get_dict(table_type, filename):
    """Create dict from files\n
    accepted table_type: 'answer' or 'question'\n
    return list of dict of strings key and values
    """
    table = get_table_from_file(filename)
    return create_dict(table, table_type)


def create_dict(table, table_type):
    dict_table = []
    if table_type == "answer":
        for row in table:
            dict_line = {}
            dict_line["answer_id"] = row[0]
            dict_line["submisson_time"] = row[1]
            dict_line["vote_number"] = row[2]
            dict_line["question_id"] = row[3]
            dict_line["message"] = row[4]
            dict_line["image"] = row[5]
            dict_table.append(dict_line)
    if table_type == "question":
        for row in table:
            dict_line = {}
            dict_line["question_id"] = row[0]
            dict_line["submisson_time"] = row[1]
            dict_line["view_number"] = row[2]
            dict_line["vote_number"] = row[3]
            dict_line["title"] = row[4]
            dict_line["message"] = row[5]
            dict_line["image"] = row[6]
            dict_table.append(dict_line)
    return dict_table


def save_dict(table, table_type, filename):
    """Save list to file\n
    accepted table_type: 'answer' or 'question'\n
    converts dict list to string list, encode and write to file.
    """
    work_table = []
    if table_type == "answer":
        for row in table:
            table_line = []
            table_line.append(row["answer_id"])
            table_line.append(row["submisson_time"])
            table_line.append(row["vote_number"])
            table_line.append(row["question_id"])
            table_line.append(row["message"])
            table_line.append(row["image"])
            work_table.append(table_line)
    if table_type == "question":
        for row in table:
            table_line = []
            table_line.append(row["question_id"])
            table_line.append(row["submisson_time"])
            table_line.append(row["view_number"])
            table_line.append(row["vote_number"])
            table_line.append(row["title"])
            table_line.append(row["message"])
            table_line.append(row["image"])
            work_table.append(table_line)
    write_table_to_file(work_table, filename)


def main():
    table = get_dict("question", "question.csv")
    for line in table:
        print("question_id", line["question_id"])
        print("submisson_time", line["submisson_time"])
        print("view_number", line["view_number"])
        print("vote_number", line["vote_number"])
        print("title", line["title"])
        print("message", line["message"])
        print("image", line["image"])
        print("\n")


if __name__ == '__main__':
    main()
