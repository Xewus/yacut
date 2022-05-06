from datetime import datetime as dt

from . import db
from .constants import api_fields

# Название класса нарушает PEP из-за тестов */tests/conftest.py:23:


class URL_map(db.Model):
    """Связывает ориганальный URL с коротким.

    Attrs:
       id: Primary key
       original: Оригинальный URL
       short: Подменный короткий URL
       timestamp: Временная метка. Defaults to utcnow.
    """
    id = db.Column(db.Integer(), primary_key=True)
    original = db.Column(db.Text(), nullable=False, index=True)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime(), default=dt.utcnow)

    def as_dict(self):
        """Преобразует данные модели в словарь.

        Returns:
            dict: Данные в виде словаря.
        """
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            api_fields['original']: self.original,
            api_fields['short']: self.short,
        }
