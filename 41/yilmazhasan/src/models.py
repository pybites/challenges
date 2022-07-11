import shared_objects
from collections import namedtuple

# import pdb
# pdb.set_trace()

db = shared_objects.db

class Tweet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(140), unique=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=True)
    user_email = db.Column(db.String(50), nullable=True)
    create_date = db.Date()
    favorite_count = db.Integer()
    retweet_count = db.Integer()

# Tip which has been used in this script is different than TipModel which I have been using
Tip = namedtuple('Tip', 'time code name published') 

#Sent tips
class TipModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # text = db.Column(db.String(140), unique=True, nullable=False)
    text = db.Column(db.String(140), unique=False, nullable=True)
    user_name = db.Column(db.String(50), nullable=True)
    user_email = db.Column(db.String(50), nullable=True)
    time = db.Date()
    code = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=True)
    published = db.Boolean()

    def __repr__(self):
        return "<Text: {}>".format(self.text)


# db.drop_all()
# db.create_all()
