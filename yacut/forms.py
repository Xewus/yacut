from flask_wtf import FlaskForm
import wtforms as fields
from . import validators

from string import ascii_letters, digits

allowed_symbols = f'{ascii_letters}{digits}'


class UrlForm(FlaskForm):
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
