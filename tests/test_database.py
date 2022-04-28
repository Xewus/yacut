from sqlalchemy import inspect

from yacut import db
from yacut.models import URL_map


def test_fields(_app):
    assert db.engine.table_names() == ['URL_map'], (
        'Не обнаружена таблица URL_map'
    )
    inspector = inspect(URL_map)
    fields = [i.key for i in inspector.mapper.column_attrs]
    assert all(field in ['id', 'original', 'short', 'timestamp'] for field in fields), (
        'В модели не найдены все необходимые поля. '
        'Проверьте модель: в ней должны быть поля id, original, short и timestamp.'
    )
