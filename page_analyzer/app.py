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
    )
from datetime import date
import os
from dotenv import load_dotenv


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
    new_url['created_at'] = date.today().strftime('%Y-%m-%d')
    parsed_url = parse_url(new_url['url'])
    errors = validate(parsed_url)
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
            )
        if 'already_exists_url' in errors.keys():
            added_url = get_by_name(parsed_url)
            id = added_url['id']
            flash(errors['already_exists_url'], 'alert-info')
            return redirect(url_for('get_url', id=id))
    else:
        new_url['url'] = parsed_url
        add_to_url_list(new_url)
        flash('Адрес добавлен', 'alert-success')
        added_url = get_by_name(parsed_url)
        id = added_url['id']
        return redirect(url_for('get_url', id=id))


@app.get('/urls')
def get_all_urls():
    all_urls = get_url_list()
    return render_template('urls.html', urls=all_urls)


@app.get('/urls/<id>')
def get_url(id):
    url = get_by_id(id)
    errors = get_flashed_messages(with_categories=True)
    return render_template('url.html', url=url, errors=errors)
