"""
views.py

Contains all the views related to pomodoro app
"""
from flask import Blueprint
from flask import render_template

from application import db
from .forms import AddTaskForm
from .models import PomoTask


pomodoro_app = Blueprint('todo_app', __name__)


@pomodoro_app.route('/')
def index():
    """
    Index page
    """
    form = AddTaskForm()
    return render_template('pomodoro/index.html', form=form)


@pomodoro_app.route('/start', methods=('GET', 'POST'))
def start():
    """
    Start task and pomodoro time
    """
    form = AddTaskForm()
    return render_template('pomodoro/index.html', form=form)
