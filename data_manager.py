import psycopg2
from private_psql_settings import connectioon_triplets


def connect_to_db():
    dbname, user, password = connectioon_triplets()


def main():
    pass

if __name__ == '__main__':
    main()