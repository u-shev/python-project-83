import requests
from bs4 import BeautifulSoup
from page_analyzer.conn_database import get_by_id
from datetime import date


def get_check(id):
    url = get_by_id(id)
    page_name = url['name']
    r = requests.get(page_name)
    html_doc = r.text
    status_code = r.status_code
    soup = BeautifulSoup(html_doc, 'html.parser')
    h1 = soup.h1.string if soup.h1 else ''
    title = soup.h1.string if soup.title else ''
    if soup.find('meta', {'name': 'description'}):
        description = soup.find('meta', {'name': 'description'})['content']
    else:
        description = ''
    check = {'url_id': id,
             'status_code': status_code,
             'h1': h1,
             'title': title,
             'description': description,
             'created_at': date.today().strftime('%Y-%m-%d'),
             }
    return check
