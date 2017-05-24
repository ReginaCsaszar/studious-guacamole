import psycopg2
from private_psql_settings import connectioon_triplets


def run_query(query):
    """
    A single query from the localhost database.
    Arg:
        @query: string - a whole executable psql query
    return:
        - for SELECT: list of tuples
        - in case of error: error message
        - "Done :)" if non SELECT query executed without error
    """
    try:
        dbname, user, password = connectioon_triplets()
        connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(dbname, user, password)
        connection = psycopg2.connect(connect_str)
        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(query)

        if query.upper().startswith("SELECT"):
            rows = cursor.fetchall()
        else:
            rows = "Done :)"
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)
        rows = exception

    finally:
        if connection:
            connection.close()
    return rows


def build_dict(table, key_words):
    """
    Build a list of dictionaries with given keys.
    Args:
        @table: list of tuples (or lists)
        @key_words: list of strings in the order of the element of tuples
    Return:
        list of dictionaries
    """
    result = []
    for row in table:
        record = {}
        for key, value in zip(key_words, row):
            record[key] = value
        result.append(record)
    return result


def main():
   pass


if __name__ == '__main__':
    main()

