from typing import Dict
from db import db

class UrlModel(db.Model):

    __tablenmae__ = "url_shorturl"

    _id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, unique=True)
    short_url = db.Column(db.Text, unique=True)

    def __init__(self, url: str, short_url: str):
        self.url = url
        self.short_url = short_url

    def to_json(self) -> Dict:
        return {"shorturl": self.short_url}


    @classmethod
    def get_item_by_url(cls, url: str):
        row = cls.query.filter_by(url=url).first()
        if row:
            return row

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()