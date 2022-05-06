import multiprocessing
import random

from sqlalchemy.exc import IntegrityError

from . import constants as const
from . import db
from .models import URL_map


def get_unique_short_id(symbols=const.allowed_symbols, length=const.LEN_AUTO_SHORT):
    """Создаёт строку из случайных символов.

    Args:
        symbols (str): Разрешённые для генерации символы.
        length (int, optional): Длина генерируемой строки. Defaults to 6.

    Returns:
        str: Сгенерированная случайноя строка.
    """
    result = []
    while True:
        for _ in range(length):
            multiprocessing.Process(result.append(random.choice(symbols)))
        result = ''.join(result)
        if URL_map.query.filter_by(short=result).first():
            result = []
            continue
        return ''.join(result)


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
        original (str): Данные для URL_map.original.
        short (str):  Данные для URL_map.short.
    Returns:
        boll: Удалось или нет добавить данные.
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
    """Получает и проверяет данные из формы.

    Args:
        form (FlaskForm): Форма с данными.

    Returns:
        tuple(str, ...): полученные данные.
    """
    original = form.original_link.data
    short = form.custom_id.data
    #  Возможны три ситуации, потому три выхода.
    #  Можно сделать два выхода, либо как было раньше череез if`ы,
    #  либо будет лишний запрос в БД со сгенерированной ссылкой,
    #  хотя его можно и отменить прикостылив флаг.
    #  В таком виде хотя бы "плоское лучше вложенного".
    #  После проверки комментарии будут удалены.
    if not short:
        return original, get_unique_short_id(), None
    if short_url_exist(short):
        return original, short, const.SHORT_URL_IS_BUSY % ('', '', short, '!')
    return original, short, None
