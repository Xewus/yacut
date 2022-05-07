"""ORM-моделя для создания таблиц в БД.
"""
from datetime import datetime as dt

from . import db


class UrlMap(db.Model):
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
