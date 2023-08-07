#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response

from treatment import usertweets

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def search():
    search_text = request.form["q"]
    tmp_text = usertweets.search_tweets(search_text)
    #print(tmp_text)
    resp = make_response(tmp_text)
    resp.status_code = 200
    resp.headers["Access-Control-ALlow-Origin"] = "*"    
    return resp

if __name__ == '__main__':
    app.run(debug=True)
