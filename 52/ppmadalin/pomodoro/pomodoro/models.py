"""
models.py

Contains all the models related pomodor app
"""
from application import db


class PomoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    stop = db.Column(db.DateTime, nullable=False)

    def __init__(self, task, start, stop):
        self.task = task
        self.start = start
        self.stop = stop

    def __repr__(self):
        return f'<Task {self.task}'
