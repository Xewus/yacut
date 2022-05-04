from flask import abort, flash, redirect, render_template, url_for

from . import app, db, forms, models, utils

@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = forms.UrlForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = utils.get_unique_short_id()
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
