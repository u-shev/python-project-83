from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import extras


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def get_url_list():
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM urls')
        url_list = curs.fetchall()
    conn.close()
    return url_list


def add_to_url_list(new_url):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s);',
                     (new_url['url'], new_url['created_at']))
    conn.commit()
    conn.close()


def get_by_id(id):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
        curs.execute('SELECT * FROM urls where id = (%s)', (id,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def get_by_name(name):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
        curs.execute('SELECT * FROM urls where name = (%s)', (name,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url
