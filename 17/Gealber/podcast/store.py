import sqlite3

class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('feeds.db')
        self.cur = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS episodes (title text, link text, description text, date text, author text)''')
        self.conn.commit()

    def add_episode(self, data):
        data = (
            data['title'],
            data['link'],
            data['description'],
            data['date'],
            data['author']
        )
        self.cur.execute("INSERT INTO episodes VALUES (?,?,?,?,?)", data)
        self.conn.commit()

    def close(self):
        self.conn.close()
