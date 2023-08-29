from datetime import date
from page_analyzer.app import DATABASE_URL
import psycopg2
from psycopg2.extras import DictCursor


def make_conn():
    return psycopg2.connect(DATABASE_URL)


def get_url_list():
    conn = make_conn()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT\
                      url_checks.url_id,\
                      MAX(url_checks.created_at) AS check_crested_at,\
                      url_checks.status_code,\
                     (SELECT name FROM urls WHERE id = url_checks.url_id)\
                      FROM url_checks\
                      GROUP BY url_checks.url_id, url_checks.status_code \
                      ORDER BY url_checks.url_id DESC')
        url_list = curs.fetchall()
    conn.close()
    return url_list


def add_to_url_list(new_url):
    conn = make_conn()
    with conn.cursor() as curs:
        curs.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s);',
                     (new_url['name'], date.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()


def get_by_id(id):
    conn = make_conn()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where id = (%s)', (id,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def get_by_name(name):
    conn = make_conn()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where name = (%s)', (name,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def add_to_check_list(url_id, status_code=None, h1='',
                      title='', description=''):
    conn = make_conn()
    with conn.cursor() as curs:
        curs.execute('INSERT INTO url_checks (url_id, status_code, h1, title,\
                      description, created_at)\
                      VALUES (%s, %s, %s, %s, %s, %s);',
                     (url_id, status_code, h1, title, description,
                      date.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()


def get_check_list(url_id):
    conn = make_conn()
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM url_checks where url_id = (%s)\
                     ORDER BY id DESC', (url_id,))
        url_checks = curs.fetchall()
    conn.close()
    return url_checks
