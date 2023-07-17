import validators
from page_analyzer.parser import parse_url
from page_analyzer.conn_database import get_url_list


def validate(url):
    errors = {}
    url_list = get_url_list()
    parsed_url = parse_url(url)
    if not url:
        errors['no_url'] = "URL обязателен"
    if url and (not validators.url(parsed_url) or len(parsed_url) > 255):
        errors['incorrect_url'] = 'Некорректный URL'
    for u in url_list:
        if u.startswith(parsed_url):
            errors['already_exists_url'] = 'Страница уже существует'
    return errors
