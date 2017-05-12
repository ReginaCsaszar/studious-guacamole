"""Data manager functions"""
import base64
import os


current_file_path = os.path.dirname(os.path.abspath(__file__))+"/data/"


def encode_string(field):
    """ Encode field, return b64.
    """
    return base64.b64encode(str.encode(field)).decode()


def decode_string(field):
    """ Decode field, return string
    """
    return base64.b64decode(str.encode(field)).decode()


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
            dict_line["message"] = decode_string(row[4])
            dict_line["image"] = decode_string(row[5])
            dict_table.append(dict_line)
    if table_type == "question":
        for row in table:
            dict_line = {}
            dict_line["question_id"] = row[0]
            dict_line["submisson_time"] = row[1]
            dict_line["view_number"] = row[2]
            dict_line["vote_number"] = row[3]
            dict_line["title"] = decode_string(row[4])
            dict_line["message"] = decode_string(row[5])
            dict_line["image"] = decode_string(row[6])
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
            table_line.append(encode_string(row["message"]))
            table_line.append(encode_string(row["image"]))
            work_table.append(table_line)
    if table_type == "question":
        for row in table:
            table_line = []
            table_line.append(row["question_id"])
            table_line.append(row["submisson_time"])
            table_line.append(row["view_number"])
            table_line.append(row["vote_number"])
            table_line.append(encode_string(row["title"]))
            table_line.append(encode_string(row["message"]))
            table_line.append(encode_string(row["image"]))
            work_table.append(table_line)
    write_table_to_file(work_table, filename)


def delete_file(path):
    os.remove(path)


def main():
    pass


if __name__ == '__main__':
    main()
