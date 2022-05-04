from datetime import datetime as dt

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=dt.utcnow)

    def from_dict(self, data):
        original = data.get['url']
        short = data.get['custom_id']
        if original and short:
            self.original = original
            self.short = short
            return
        raise

    def as_dict(self):
        return dict(
            id=self.id,
            url=self.original,
            custom_id=self.short,
            timestamp=self.timestamp
        )
