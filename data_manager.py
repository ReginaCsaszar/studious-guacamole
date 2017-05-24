import psycopg2
from private_psql_settings import connectioon_triplets


def run_query(query):
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


def main():
    result = run_query("SELECT * FROM question;")
    print(result)

if __name__ == '__main__':
    main()

