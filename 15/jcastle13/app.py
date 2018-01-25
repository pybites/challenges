from flask import Flask, render_template

# persistence
#
# could go with serialization
# import shelve
# or:
# import pickle
#
# could go with stdlib DB
# import sqlite3
# 
# could go with ORM
# $ pip install flask_sqlalchemy
# add:
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run(debug=True)
