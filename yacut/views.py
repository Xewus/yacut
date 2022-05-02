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
        if not models.UrlMap.query.filter_by(short=result).first():
            return result
        result = []


@app.route('/', methods=('GET', 'POST'))
def index_view():
    print(app.root_path)
    form = forms.UrlForm()
    if form.validate_on_submit():
        short_url = form.short_url.data
        if not short_url:
            short_url = get_unique_short_id(allowed_symbols)
        elif models.UrlMap.query.filter_by(short=short_url).first():
            flash('Такое сокращение уже занято')
            return render_template('index.html', form=form)

        long_url = form.long_url.data
        url_map = models.UrlMap(
            original=long_url,
            short=short_url
        )
        flash(short_url)
        db.session.add(url_map)
        db.session.commit()
        return redirect(url_for('index_view'))
    return render_template('index.html', form=form)


@app.route('/<string:short_url>')
def mapper(short_url):
    original_url = models.UrlMap.query.filter_by(short=short_url).first()
    return redirect(original_url.original)
