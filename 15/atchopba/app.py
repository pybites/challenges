from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///player.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Player(db.Model):
    #
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return "<%s %s>" % self.firstname, self.lastname
    
db.drop_all()
db.create_all()


@app.route('/')
def player_list():
    players = Player.query.all()
    return render_template("list.html", players=players)

@app.route("/player", methods=["POST"])
def add_player():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    if not firstname or not lastname:
        return "Error"
    #
    player = Player(firstname, lastname)
    db.session.add(player)
    db.session.commit()
    return redirect("/")

@app.route("/delete/<int:player_id>")
def delete_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return redirect("/")
    db.session.delete(player)
    db.session.commit()
    return redirect("/")

@app.route("/done/<int:player_id>")
def resolve_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return redirect("/")
    if player.done:
        player.done = False
    else:
        player.done = True
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
