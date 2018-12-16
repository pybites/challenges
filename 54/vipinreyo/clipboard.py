"""A simple Python script to capture the data copied to Clipboard and store it persistently

Pre-requisites:
Python 3 runtime
python3 -m venv venv - Create a Virtual environment
pip install -r requirements.txt - Install the required module, which is pyperclip
"""

import pyperclip
import sqlite3
from datetime import datetime


class ClipBoard:
    CLIPBOARD_DB = 'clipboard.db'

    def __init__(self):
        """Initialisation method to initialise clipboard DB and run cleanup routines"""
        self._create_db_and_initialize_table()

    def _create_db_and_initialize_table(self):
        """Helper method to initialize db"""

        with sqlite3.connect(self.CLIPBOARD_DB) as conn:
            cur = conn.cursor()
            clipboard_data_table = """CREATE TABLE IF NOT EXISTS clipboard_data (
                                date text,
                                data text);"""
            cur.execute(clipboard_data_table)

    def get_clipboard_history(self):
        """Method to retrieve the historical clipboard data from a Sqllite DB and return as a list"""

        with sqlite3.connect(self.CLIPBOARD_DB) as conn:
            cur = conn.cursor()
            sql = "SELECT * from clipboard_data;"
            cur.execute(sql)
            return [row for row in cur.fetchall()]

    def add_data_to_db(self, data):
        """Method to add clipboard data to the database"""
        with sqlite3.connect(self.CLIPBOARD_DB) as conn:
            cur = conn.cursor()
            sql = "INSERT INTO clipboard_data (date, data) values (?, ?)"
            cur.execute(sql, [datetime.now().strftime('%d-%m-%Y %H:%M:%S'), data])


def main():
    cb = ClipBoard()
    cb.add_data_to_db(pyperclip.paste())
    print(cb.get_clipboard_history())


if __name__ == '__main__':
    main()

