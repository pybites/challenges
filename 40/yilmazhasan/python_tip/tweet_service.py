from collections import defaultdict
from collections import defaultdict
import tweepy
import os
import sqlalchemy as db
from .models import *
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from .config import *
import pdb

class TweetService:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def get_tweets_from_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)
        user = api.get_user("python_tip")
        alltweets = []

        tweets_with_replies = api.user_timeline(screen_name = 'python_tip', count = 3000, include_rts = True)
        tweet_replies = list(filter(lambda x : x.in_reply_to_user_id, tweets_with_replies))
        tweets = list(filter(lambda x : not x.in_reply_to_user_id, tweets_with_replies))
        pdb.set_trace()
        return tweets

    def get_hashtag_freqs(self, tweets):

        hashtag_freqs = defaultdict(int)

        for tweet in tweets:
            tweet.byUser =  tweet.entities['user_mentions'][0]['screen_name'] if tweet.entities['user_mentions'] and tweet.entities['user_mentions'][0]['screen_name'] else ""
        # import pdb
        # pdb.set_trace()
            for hashtag in tweet.entities['hashtags']:
                hashtag_freqs[hashtag['text'].lower()] += 1
        
        return hashtag_freqs
