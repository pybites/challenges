"""
forms.py

Contains add new task form
"""
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField


class AddTaskForm(FlaskForm):
    task = StringField('Task', [validators.InputRequired(),
                                validators.Length(min=5, max=80)])
