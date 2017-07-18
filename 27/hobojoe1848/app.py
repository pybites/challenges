#!python3

from flask import Flask, render_template

import praw

app = Flask(__name__)

reddit = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='')

@app.route('/', methods=['GET', 'POST'])
def index():
    tifu_subs = {}
    til_subs = {}
    for submission in reddit.subreddit('TIFU').hot(limit=20):
        tifu_subs[submission.title] = submission.shortlink
    
    for submission in reddit.subreddit('todayilearned').hot(limit=20):
        til_subs[submission.title] = submission.shortlink
    
    return render_template('index.html',
                            tifu_subs=tifu_subs,
                            til_subs=til_subs)            

if __name__ == "__main__":
    app.run()
