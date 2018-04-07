import os
import time

from datetime import datetime


def check_dir(dir):
    """Checks to see if a certain directory exist
    
    Creates it if it doesn't"""
    pwd = os.path.curdir
    app_path = os.path.join(os.path.abspath(pwd))
    dir_path = os.path.join(app_path, dir)

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def format_link(link):
    """Removes extra parameters from file link if they exist"""
    if '?' in link:
        return link.split('?')[0]
    else:
        return link


def format_duration(seconds):
    """Converts seconds into hh:mm:ss format"""
    if ':' in seconds:
        return seconds
    else:
        m, s = divmod(int(seconds), 60)
        h, m = divmod(m, 60)
        return f'{h:02}:{m:02}:{s:02}'


def format_date(date_struct):
    """Format the published date"""
    return datetime.fromtimestamp(time.mktime(date_struct))