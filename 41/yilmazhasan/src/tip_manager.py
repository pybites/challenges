import os
import sys
import pdb

from flask import Flask
from flask import g, session, request, url_for, flash
from flask import redirect, render_template
from flask_oauthlib.client import OAuth
from functools import wraps

from flask_sqlalchemy import SQLAlchemy

import datetime

import schedule
import time
import threading

# custom modules
import shared_objects
import config
import models
import db_service


# import objects from shared_objects module 
db = shared_objects.db
app = shared_objects.app
db_service = db_service.db_service_instance
Tweet = models.Tweet
TipModel = models.TipModel

tweets = db_service.get_tweets()
tips = db_service.get_tips()

oauth = shared_objects.oauth
twitter = shared_objects.twitter

current_user_name = None

# ----------------- Schedule region ----------------- 
def update_db():
    print ("updating db")
    db_service.clear_all_tweets_in_db()
    tweets = db_service.get_tweets()
    db_service.save_tweets_to_db()
    print ("updated db")

schedule.every(1).hour.do(update_db)

def check_scheduled_db_task():
    while True: 
    
        # Checks whether a scheduled task is pending to run or not 
        schedule.run_pending() 
        print("sleep")
        time.sleep(3000) # seconds

print("Main    : before creating thread")
x = threading.Thread(target=check_scheduled_db_task, args=(1,))
print("Main    : before running thread")
x.start()
print("Main    : wait for the thread to finish")
x.join()
print("Main    : all done")
# ----------------- end region ----------------- 

# ----------------- OAUTH REGION -----------------

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('authorize', next=request.args.get('next') or request.referrer or None))

@app.route('/logout')
def logout():
    global current_user_name
    current_user_name = None
    session.pop('screen_name', None)
    flash('You were signed out')
    return redirect(request.referrer or url_for('index'))

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user_name is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/authorize')
def authorize():
    global current_user_name
    next_url = request.args.get('next') or url_for('home')
    next_url = next_url[1:] if next_url[0] == '/' else next_url # remove the first slash in order to be able to use in url_for later
    
    resp = twitter.authorized_response()
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)
    
    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )

    session['twitter_user'] = resp['screen_name']
    flash('You were signed in as %s' % resp['screen_name'])
    
    current_user_name = resp['screen_name']
    session['username'] = resp['screen_name']

    return redirect( next_url)

# ----------------- END REGION -----------------

@app.route("/", methods=["GET", "POST"])
@require_login
def index():
    # return redirect(url_for("home"))
    return render_template("index.html", current_user_name = current_user_name)  

# ----------------- DB OPERAIONS -----------------

@app.route("/home", methods=["GET", "POST"])
@require_login
def home():
    bag = dict(message="Add a tip")

    tips = db_service.get_tips()
    tweets = db_service.get_tweets()
    return render_template("home.html", tweets=tweets, bag=bag, tips=tips, current_user_name = current_user_name)  

@app.route("/new-tip", methods=["GET", "POST"])
@require_login
def new_tip():
    error = ""
    result = dict()
    try:
        if request.form:
            tip = TipModel(text=request.form.get("text"), user_name=request.form.get("user_name"), user_email=request.form.get("user_email"))
            tip.code = tip.text
            tip.name = tip.user_name
            tip.time = datetime.datetime.now()
            tip.published = False
            print(tip)
            result = db_service.add_tip(tip)
            result['searched'] = True

    except Exception as exc:
        db.session.rollback()
        error = exc
    finally:
        tips = TipModel.query.all()
    return render_template("home.html", tweets=tweets, tips=tips, bag=result, current_user_name = current_user_name)  

@app.route("/update_tip", methods=["POST"])
@require_login
def update_tip():
    id = request.form.get("id")
    newtext = request.form.get("newtext")
    oldtext = request.form.get("oldtext")
    oldtext = request.form.get("oldtext")
    db_service.update_tip(id, newtext, is_published=True)
    return redirect("/home")

@app.route("/delete_tip", methods=["POST"])
@require_login
def delete_tip():
    id = request.form.get("id")
    db_service.delete_tip(id)
    return redirect("/home")

# ----------------- END REGION -----------------

if __name__ == "__main__":
    app.run(debug=True)