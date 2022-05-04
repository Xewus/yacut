from random import choice

from . import models
from . constants import allowed_symbols


def get_unique_short_id(symbols=allowed_symbols, length=6):
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
        if not models.URL_map.query.filter_by(short=result).first():
            return result
        result = []


def short_url_exist(short_url, model):
    """Проверяет наличие в таблице данных по полю `short`.

    Args:
        short_url (string): Проверяемые данные.
        model (db.Model): Модель связанная с таблицей в БД.

    Returns:
        bool: Наличие либо отсутствие записи с указанными данными.
    """
    return bool(model.query.filter_by(short=short_url).first())
