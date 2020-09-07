from collections import defaultdict

import tweepy
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from difflib import SequenceMatcher

import pdb
import models
import config
import shared_objects

from contextlib import closing
import codecs
import csv
import ssl
import sys

import models

import shared_objects

import pdb

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


Tweet = models.Tweet
TipModel = models.TipModel
db = shared_objects.db


LOCAL_CSV = config.LOCAL_CSV  # for testing
REMOTE_CSV = config.REMOTE_CSV
FIELDS = config.FIELDS
CONTEXT = config.CONTEXT
TEST = config.TEST


class DbService:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, db):

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self.db = db
        self.tweets = self.get_tweets()
        self.tips = self.get_tips()


    # ---------- Basic CRUD operations ----------

    def add_tweet(self, tweet):
        # pdb.set_trace()
        submittedBefore = self.anySimilarTipSubmittedBefore(tweet.text)
        if(not submittedBefore) :
            try:
                self.db.session.add(tweet)
                self.db.session.commit()
                self.tweets.append(tweet)
                return ""
            except Exception as exc:
                raise exc

        else:
            return "There is found a similar one, please try a different tip!"

    def add_tip(self, tip):
        res = self.anySimilarTipSubmittedBefore(tip.text)
        if(not res) :
            try:
                self.db.session.add(tip)
                self.db.session.commit()
                self.tips.append(tip)
                return ""
            except Exception as exc:
                raise exc
            return dict (message = "Added Successfully")
        else:
            similar_tip_id = res['similar_tip_id']
            is_published = res['is_published']
            return dict (message = "There is found a similar one, please try a different tip!", similar_tip_id = similar_tip_id, is_published=is_published)

    def get_tweet(self, id):
        tweet = Tweet.query.filter_by(id=id).first()
        return tweet

    def get_tip(self, id):
        tip = TipModel.query.filter_by(id=id).first()
        return tip

    def update_tweet(self, id, text):
        tweet = Tweet.query.filter_by(id=id).first()
        print (tweet)
        tweet.text = text
        self.db.session.commit()
        return tweet

    def update_tip(self, id, text, is_published):
        tip = TipModel.query.filter_by(id=id).first()
        print (tip)
        tip.text = text
        tip.published = is_published
        self.delete_tip(id)
        self.add_tweet(Tweet(text=tip.text, user_name = tip.user_name))
        # self.tweets = [Tweet(text=tip.text, user_name = tip.user_name)] + self.tweets
        self.db.session.commit()
        return tip

    def delete_tweet(self, id):
        tweet = Tweet.query.filter_by(id=id).first()
        self.db.session.delete(tweet)
        self.db.session.commit()
        self.tweets = list(filter(lambda x: x.id != id, self.tweets))

    def delete_tip(self, id):
        tip = TipModel.query.filter_by(id=id).first()
        self.db.session.delete(tip)
        self.db.session.commit()
        self.tips = list(filter(lambda x: str(x.id) != str(id), self.tips))

    # ---------- Basic operations END ----------

    # ---------- Tip Db & Remote operations ----------

    # Submitted tips
    def get_csv_entries(self):
        if TEST:
            action = open(LOCAL_CSV)
        else:
            action = closing(urlopen(REMOTE_CSV, context=CONTEXT))
        with action as f:
            if not TEST and sys.version_info.major > 2:
                f = codecs.iterdecode(f, 'utf-8')  # needed for urlopen and py3
            entries = []
            for entry in csv.DictReader(f, fieldnames=FIELDS):
                # yield entry
                entries.append(entry)
            return entries

    # first check from db if not exists then take from api
    def get_tips(self):
        tips = TipModel.query.all()
        if tips: # add all to db
            return tips
        else:
            tips = self.get_csv_entries()
            for tip in tips:
                try:
                    tip = TipModel(time=tip['time'], code = tip['code'], name=tip['name'], user_name=tip['name'], published=tip['published'], text=tip['code'])
                    db.session.add(tip)
                except Exception as E:
                    db.session.rollback()
                    db.session.commit()
                    continue
                print("A tip added to db")
            db.session.commit()
            print("Commited")
        return self.get_tips()

    def get_all_tips_in_db(self):
        tips = TipModel.query.all()

        return tips

    # ---------- Tip Db & Remote operations END ----------

    # ---------- Tweet Db & Remote operations ----------
    def get_tweets_from_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)
        user = api.get_user("python_tip")
        alltweets = []

        # tweets = api.user_timeline(screen_name = 'python_tip', include_rts = True)
        tweets = api.user_timeline(screen_name = 'python_tip', count=3000, include_rts = True)
        return tweets

    # first check from db if not exists then take from api
    def get_tweets(self):
        self.tweets = Tweet.query.all() or []
        if not self.tweets:
            tweets_from_api = self.get_tweets_from_api()
            for tweet in tweets_from_api:
                byUser =  tweet.entities['user_mentions'][0]['screen_name'] if tweet.entities['user_mentions'] and tweet.entities['user_mentions'][0]['screen_name'] else ""
                self.tweets.append(Tweet(text = tweet.text, user_name=byUser or "anonym", create_date=tweet.created_at, favorite_count=tweet.favorite_count, retweet_count=tweet.retweet_count))

        return self.tweets

    def save_tweets_to_db(self, tweets=[]):
        tweets = tweets or self.tweets

        for tweet in tweets:
            self.db.session.add(Tweet(text = tweet.text, user_name=byUser or "anonym", create_date=tweet.created_at, favorite_count=tweet.favorite_count, retweet_count=tweet.retweet_count))
        self.db.session.commit()

    def get_all_tweets_in_db(self):
        tweets = Tweet.query.all()

        return tweets

    def clear_all_tweets_in_db(self):
        tweets = Tweet.query.all()

        try:
            for tweet in tweets:
                self.db.session.delete(tweet)
            self.db.session.commit()
            self.tweets  =[]
        except Exc:
            return False

        return True

    # ---------- Tweet Db & Remote operations END ----------

    # --------- Helper functions ---------
    def get_hashtag_freqs(self,tweets):

        hashtag_freqs = defaultdict(int)

        for tweet in tweets:
            tweet.byUser =  tweet.entities['user_mentions'][0]['screen_name'] if tweet.entities['user_mentions'] and tweet.entities['user_mentions'][0]['screen_name'] else ""

        for hashtag in tweet.entities['hashtags']:
            hashtag_freqs[hashtag['text']] += 1
        
        return hashtag_freqs

    def anySimilarTipSubmittedBefore(self, text):
        # pdb.set_trace()
        similarity = 0

        for idx, tweet in enumerate(self.tweets):
            similarity = self.getSimiliarityRatio(text, tweet.text)        
            # print(similarity)
            if similarity > 0.5:
                return dict(is_published = True, similar_tip_id=idx)

        for idx, tip in enumerate(self.tips):
            similarity = self.getSimiliarityRatio(text, tip.text)        
            # print(similarity)
            if similarity > 0.5:
                return dict(is_published = False, similar_tip_id=idx)
        return None
        
    def getSimiliarityRatio(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

db_service_instance = DbService(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret, shared_objects.db)
