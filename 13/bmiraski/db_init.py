import sqlite3

db = sqlite3.connect('movies.db')

db.execute("DROP TABLE IF EXISTS movies")
db.execute("""CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    director TEXT NOT NULL,
    movie_title TEXT NOT NULL,
    year INTEGER,
    score FLOAT NOT NULL
)""")
db.commit()

db.close()
