from random import choice
from sqlalchemy.exc import IntegrityError

from . import db
from . import constants as const
from . models import URL_map


def get_unique_short_id(symbols=const.allowed_symbols, length=6):
    """Создаёт строку из случайных символов.

    Args:
        symbols (_type_): _description_
        length (int, optional): _description_. Defaults to 6.

    Returns:
        _type_: _description_
    """
    result = []
    while True:
        for i in range(length):
            result.append(choice(symbols))
        result = ''.join(result)
        if not URL_map.query.filter_by(short=result).first():
            return result
        result = []


def short_url_exist(short_url):
    """Проверяет наличие в таблице данных по полю `short`.

    Args:
        short_url (string): Проверяемые данные.
        model (db.Model): Модель связанная с таблицей в БД.

    Returns:
        bool: Наличие либо отсутствие записи с указанными данными.
    """
    return bool(URL_map.query.filter_by(short=short_url).first())


def add_url_map(original, short):
    """Добавляет данные в БД.

    Args:
        original (_type_): _description_
        short (_type_): _description_
    """
    url_map = URL_map(
        original=original,
        short=short
    )
    db.session.add(url_map)
    try:
        db.session.commit()
    except IntegrityError:
        return False
    return True


def get_urls_for_map(form):
    original = form.original_link.data
    short = form.custom_id.data
    if short:
        if short_url_exist(short):
            return original, short, const.SHORT_URL_IS_BUSY % ('', '', short, '!')
    else:
        short = get_unique_short_id()
    return original, short, None