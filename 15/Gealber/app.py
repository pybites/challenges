from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cards = db.relationship('Card', backref='user', lazy=True)
    date_created = db.Column(db.DateTime, default=datetime.now)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    name = db.Column(db.String(50))
    description = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method == 'POST':
        username = session['username']
        user = User.query.filter_by(name=username).first()
        url = request.form['url']
        name = request.form['image_name']
        description = request.form['description']
        card = Card(url=url, name=name,
                    description=description, user_id=user.id)
        db.session.add(card)
        db.session.commit()
        return render_template('profile.html',
                               context=Card.query.filter_by(user_id=user.id).all())
    elif 'username' in session:
        return render_template('session.html', username=session['username'])
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        user = User(name=session['username'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
