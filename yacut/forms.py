import wtforms as fields
from flask_wtf import FlaskForm

from . import validators
from .constants import allowed_symbols


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
        label='Введите название до 16 символов',
        validators=(
            validators.Optional(),
            validators.Length(
                max=16,
                message='Слишком длинная'
            ),
            validators.AllOf(
                values=allowed_symbols,
                message='Разрешены только латиница и цифры'
            )
        )
    )
    submit = fields.SubmitField(
        label='Сгенерировать'
    )
