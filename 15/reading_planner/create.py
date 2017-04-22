'''http://flask-sqlalchemy.pocoo.org/2.1/quickstart/'''
from reading import db

db.drop_all()
db.create_all()
db.session.commit()
