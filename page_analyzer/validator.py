import validators
from page_analyzer.normalizer import normalize_url


def validate(url):
    errors = {}
    normalized_url = normalize_url(url)
    if not url:
        errors['no_url'] = "URL обязателен"
    if url and (not validators.url(normalized_url)
                or len(normalized_url) > 255):
        errors['incorrect_url'] = 'Некорректный URL'
    return errors
