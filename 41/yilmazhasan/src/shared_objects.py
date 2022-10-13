import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

from flask_oauthlib.client import OAuth

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret


# Sqlite configs
project_dir = project_dir = os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__),"..")))
database_file = "sqlite:///{}".format(os.path.join(project_dir, config.databasename))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

twitter = oauth.remote_app(
    'twitter',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize'
)
