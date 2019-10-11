# project/server/models.py


import datetime

from project.server import app, db


class Rate(db.Model):

    __tablename__ = "rates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.String(255), nullable=False)
    price = db.Column(db.DECIMAL(), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, currency, price, timestamp=datetime.datetime.utcnow()):
        self.currency = currency
        self.price = price
        self.registered_on = timestamp

    def __repr__(self):
        return '<Rate {0}>'.format(self.currency)
