from flask import (
    Flask,
    render_template,
    request, redirect,
    url_for,
    flash,
    get_flashed_messages
)
from page_analyzer.parser import parse_url
from page_analyzer.validator import validate
from page_analyzer.conn_database import (
    get_url_list,
    add_to_url_list,
    get_by_id,
    get_by_name,
    add_to_check_list,
    get_check_list,
)
import os
import requests
from dotenv import load_dotenv
from page_analyzer.checks import get_check


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template(
        'main.html')


@app.post('/urls')
def add_new_url():
    new_url = request.form.to_dict()
    parsed_url = parse_url(new_url['url'])
    errors = validate(parsed_url)
    same_url = get_by_name(parsed_url)
    if errors:
        if 'no_url' in errors.keys():
            flash(errors['no_url'], 'alert-danger')
            errors = get_flashed_messages(with_categories=True)
            return render_template(
                'main.html',
                new_url=new_url,
                errors=errors
            )
        if 'incorrect_url' in errors.keys():
            flash(errors['incorrect_url'], 'alert-danger')
            errors = get_flashed_messages(with_categories=True)
            return render_template(
                'main.html',
                new_url=new_url,
                errors=errors
            ), 422
    elif same_url:
        added_url = get_by_name(parsed_url)
        id = added_url['id']
        flash('Страница уже существует', 'alert-info')
        return redirect(url_for('get_url', id=id))
    else:
        new_url['name'] = parsed_url
        add_to_url_list(new_url)
        flash('Страница успешно добавлена', 'alert-success')
        added_url = get_by_name(parsed_url)
        id = added_url['id']
        return redirect(url_for('get_url', id=id))


@app.get('/urls')
def get_all_urls():
    all_urls = get_url_list()
    return render_template('urls.html', urls=all_urls)


@app.get('/urls/<int:id>')
def get_url(id):
    url = get_by_id(id)
    checks = get_check_list(id)
    errors = get_flashed_messages(with_categories=True)
    return render_template('url.html', url=url, errors=errors, checks=checks)


@app.post('/urls/<int:id>/checks')
def add_new_check(id):
    url = get_by_id(id)
    page_name = url['name']
    try:
        response = requests.get(page_name)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        flash('Произошла ошибка при проверке', 'alert-danger')
        return redirect(url_for('get_url', id=id))
    else:
        r = requests.get(page_name)
        html_doc = r.text
        status_code = r.status_code
        h1, title, description = get_check(html_doc)
        add_to_check_list(id, status_code=status_code, h1=h1,
                          title=title, description=description)
        flash('Страница успешно проверена', 'alert-success')
        return redirect(url_for('get_url', id=id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='Страница не найдена'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html',
                           message='Внутренняя ошибка сервера'), 500
