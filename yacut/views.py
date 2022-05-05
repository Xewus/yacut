from flask import abort, flash, redirect, render_template

from . import app
from . import constants as const
from . import db, forms, models, utils


@app.route('/', methods=('GET', 'POST'))
def index_view():
    """Главная страница с формой для генерации коротких ссылок.

    Returns:
        str: HTML-страница
    """
    form = forms.UrlMapForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url:
            if utils.short_url_exist(short_url, models.URL_map):

                flash(const.SHORT_URL_IS_BUSY % short_url)
                return render_template('index.html', form=form)
        else:
            short_url = utils.get_unique_short_id()

        url_map = models.URL_map(
            original=form.original_link.data,
            short=short_url
        )
        flash(const.YOUR_URL_IS_READY)
        flash(short_url)
        db.session.add(url_map)
        db.session.commit()
    return render_template('index.html', form=form)


@app.route('/<string:short_url>')
def mapper(short_url):
    """Перенаправляет с короткой ссылки на оригинальную.

    Args:
        short_url (str): Короткое имя.

    Returns:
        Responce: Перенапрвление на оригинальную ссылку.
    """
    original_url = models.URL_map.query.filter_by(short=short_url).first()
    if original_url is None:
        abort(404)
    return redirect(original_url.original)
