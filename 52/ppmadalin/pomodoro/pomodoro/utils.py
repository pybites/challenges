"""
utils.py

Contains functions which start and stop pomodoro time
"""

from datetime import datetime
from datetime import timedelta


def start():
    """
    Start pomodoro time
    """
    default = timedelta(minutes=25)
    start_time = datetime.now + default
    return start_time


def stop():
    """
    Stop pomodoro time
    """
    pass
