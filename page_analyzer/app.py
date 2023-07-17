from flask import (
    Flask,
    render_template,
    request, redirect,
    url_for,
    flash,
    get_flashed_messages
    )
from page_analyzer.validator import validate
from page_analyzer.conn_database import (
    get_url_list,
    add_to_url_list,
    get_by_id,
    get_by_name
    )
from datetime import date

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'main.html')


@app.post('/urls')
def add_new_url():
    new_url = request.form.to_dict()
    new_url['created_at'] = date.today().strftime('%Y-%m-%d')
    errors = validate(new_url)
    if errors:
        if 'no_url' in errors.keys():
            flash(errors['no_url'], 'alert-danger')
        if 'incorrect_url' in errors.keys():
            flash(errors['incorrect_url'], 'alert-danger')
        if 'already_exists_url' in errors.keys:
            url = get_by_name(new_url['url'])
            id = url['id']
            flash(errors['already_exists_url'], 'alert-info')
            return redirect(url_for('get_url', id=id))
        errors = get_flashed_messages(with_categories=True)
        return render_template(
            'index.html',
            new_url=new_url,
            errors=errors
        )
    else:
        add_to_url_list(new_url)
        flash('Адрес добавлен', 'alert-success')
        id = get_by_name(new_url['url'])['id']
        return redirect(url_for('get_one_url', id=id))


@app.get('/urls')
def get_all_urls():
    all_urls = get_url_list()
    return render_template('urls.html', urls=all_urls)


@app.get('/urls/<int:id>')
def get_url(id):
    url = get_by_id(id)
    messages = get_flashed_messages(with_categories=True)
    return render_template('url.html', url=url, messages=messages)
