from flask import Flask
from flask_restful import Api

from resources.urlshortner import UrlShortner

app = Flask(__name__)
app.secret_key = 'secretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UrlShortner, '/shortendurl/')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)