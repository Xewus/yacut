from email import message
from random import choice

from flask import abort, flash, redirect, render_template, url_for

from . import app, db, forms, models

from string import ascii_letters, digits

allowed_symbols = f'{ascii_letters}{digits}'


def get_unique_short_id(symbols, length=6):
    result = []
    while True:
        for i in range(length):
            result.append(choice(symbols))
        result = ''.join(result)
        if not models.URL_map.query.filter_by(short=result).first():
            return result
        result = []


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = forms.UrlForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = get_unique_short_id(allowed_symbols)
        elif models.URL_map.query.filter_by(short=short_url).first():
            flash(f'Имя {short_url} уже занято!')
            return render_template('index.html', form=form)

        original_link = form.original_link.data
        url_map = models.URL_map(
            original=original_link,
            short=short_url
        )
        flash('Ваша новая ссылка готова:\n')
        flash(short_url)
        db.session.add(url_map)
        db.session.commit()
    return render_template('index.html', form=form)


@app.route('/<string:short_url>')
def mapper(short_url):
    original_url = models.URL_map.query.filter_by(short=short_url).first()
    if original_url is None:
        abort(404)
    return redirect(original_url.original)
