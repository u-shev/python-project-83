import validators
from page_analyzer.parser import parse_url


def validate(url):
    errors = {}
    parsed_url = parse_url(url)
    if not url:
        errors['no_url'] = "URL обязателен"
    if url and (not validators.url(parsed_url) or len(parsed_url) > 255):
        errors['incorrect_url'] = 'Некорректный URL'
    return errors
