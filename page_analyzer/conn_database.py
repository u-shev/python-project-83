from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import DictCursor


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def get_url_list():
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT urls.id, urls.name, url_checks.status_code,\
                      url_checks.created_at AS check_created_at\
                      FROM urls\
                      LEFT JOIN url_checks ON urls.id = url_id\
                      AND url_checks.id = (SELECT MAX(url_checks.id)\
                      FROM url_checks WHERE url_id = urls.id)\
                      ORDER BY url_checks.created_at DESC')
        url_list = curs.fetchall()
    conn.close()
    return url_list


def add_to_url_list(new_url):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s);',
                     (new_url['name'], new_url['created_at']))
    conn.commit()
    conn.close()


def get_by_id(id):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where id = (%s)', (id,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def get_by_name(name):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where name = (%s)', (name,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def add_to_check_list(check):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute('INSERT INTO url_checks (url_id, status_code, h1, title,\
                      description, created_at)\
                      VALUES (%s, %s, %s, %s,%s, %s);',
                     (check['url_id'],
                      check['status_code'],
                      check['h1'],
                      check['title'],
                      check['description'],
                      check['created_at'],
                      )
                     )
    conn.commit()
    conn.close()


def get_check_list(id):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM url_checks where url_id = (%s)', (id,))
        url_checks = curs.fetchall()
    conn.close()
    return url_checks


# def get_last_check():
#     conn = psycopg2.connect(DATABASE_URL)
#     with conn.cursor(cursor_factory=DictCursor) as curs:
#         curs.execute('SELECT urls.id, urls.name,\
#                       url_checks.status_code, url_checks.created_at\
#                       FROM urls\
#                       LEFT JOIN url_checks ON urls.id = url_id\
#                       AND url_checks.id = (SELECT MAX(url_checks.id)\
#                       FROM url_checks WHERE url_id = urls.id)\
#                       ORDER BY url_checks.created_at DESC')
#         last_check = curs.fetchall()
#     conn.close()
#     return last_check
