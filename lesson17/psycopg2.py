import psycopg2
from config import host, user, password, db_name
from request import users, product, meal


connection = None


def connection_db():
    global connection
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            user_id = users(cursor)
            product_id = product(cursor)
            meal(cursor, user_id, product_id)
    except Exception as err:
        print(f'Error while worked with PostgreSQL {err}')


connection_db()
