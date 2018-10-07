import sqlite3

db = sqlite3.connect('inventory.db', detect_types=sqlite3.PARSE_DECLTYPES)

db.execute('''DROP TABLE IF EXISTS room''')
db.execute('''DROP TABLE IF EXISTS items''')
db.execute('''CREATE TABLE room (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT UNIQUE NOT NULL
           )''')
db.execute('''CREATE TABLE items (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           room_id INTEGER NOT NULL,
           item_name TEXT NOT NULL,
           item_value FLOAT(9,2),
           FOREIGN KEY (room_id) REFERENCES room (id)
           )''')
db.commit()

db.close()
