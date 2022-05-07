"""Формы для web-интерфейса.
"""
import wtforms as fields
from flask_wtf import FlaskForm

from . import constants as const
from . import validators


class UrlMapForm(FlaskForm):
    """Форма для `/index_view()`.

    Attrs:
        original_link: Оригинальная ссылка.
        custom_id: Короткое имя.
        submit: Кнопка подтверждения.
    """
    original_link = fields.URLField(
        label='Введите длинную ссылку',
        validators=(
            validators.DataRequired(
                message='Обязательное поле'
            ),
            validators.URL(
                message='Некорректный URL'
            )
        )
    )
    custom_id = fields.StringField(
        label='Введите название до %s символов' % const.MAX_LEN_SHORT,
        validators=(
            validators.Optional(),
            validators.Length(
                max=const.MAX_LEN_SHORT,
                message='Слишком длинное имя'
            ),
            validators.AllOf(
                values=const.ALLOWED_SYMBOLS,
                message='Разрешены только латиница и цифры'
            )
        )
    )
    submit = fields.SubmitField(
        label='Сгенерировать'
    )
