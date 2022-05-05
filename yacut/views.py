from email import message
from flask import abort, flash, redirect, render_template

from . import app
from . import constants as const
from . import forms, models, utils


@app.route('/', methods=('GET', 'POST'))
def index_view():
    """Главная страница с формой для генерации коротких ссылок.

    Returns:
        str: HTML-страница
    """
    form = forms.UrlMapForm()
    if form.validate_on_submit():
        original, short_url, err_message = utils.get_urls_for_map(form)
        if err_message:
            flash(err_message)
            return render_template('index.html', form=form)

        if not utils.add_url_map(original, short_url):
            flash(const.BD_ERROR)
            return render_template('index.html', form=form)

        flash(const.YOUR_URL_IS_READY)
        flash(short_url)
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
