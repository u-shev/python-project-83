import validators
from page_analyzer.parser import parse_url
from page_analyzer.conn_database import get_by_name


def validate(url):
    errors = {}
    parsed_url = parse_url(url)
    same_url = get_by_name(url)
    if len(url) == 0:
        errors['no_url'] = "URL обязателен"
    if url and (not validators.url(parsed_url) or len(parsed_url) > 255):
        errors['incorrect_url'] = 'Некорректный URL'
    if same_url:
        errors['already_exists_url'] = 'Страница уже существует'
    return errors
