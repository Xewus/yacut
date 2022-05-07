"""Функции и классы для проверок.
"""
from wtforms import validators

from . import constants as const

DataRequired = validators.DataRequired
Length = validators.Length
Optional = validators.Optional
URL = validators.URL
ValidationErr = validators.ValidationError


def len_validation(sequense, exception, min=1, max=1):
    """Проверяет длину последовательности.

    Args:
        sequense (Sequense): Проверяемая последовательность.
        exception (Exception): Поднимаемая ошибка.
        min (int, optional): Минимальная длина. Defaults to 1.
        max (int, optional): Максимальная длина. Defaults to 1.

    Raises:
        AttributeError: Если переданная дана не содержит атрибут `len`.
        exception: Неправильная длина.
    """
    try:
        getattr(sequense, '__len__')
    except AttributeError:
        raise AttributeError
    if min <= len(sequense) <= max:
        return
    raise exception


def symbols_validation(string, exception):
    """Проверяет на допустимость сиволов в строке.

    Args:
        string (string): Проверяемая строка.
        exception (Exception): Поднимаемая ошибка.

    Raises:
        exception:При наличии недопустимых символов.
    """
    if isinstance(string, str) and all((symbol in const.ALLOWED_SYMBOLS) for symbol in string):
        return
    raise exception


class AllOf(validators.AnyOf):
    """Класс подключабщий валидацию в форму.

    Проверяет допустимость символов.
    """
    def __call__(self, form, field):
        if self.message is None:
            self.message = f'Some element of {field.data} not in {self.values}'
        symbols_validation(field.data, validators.ValidationError(self.message))
