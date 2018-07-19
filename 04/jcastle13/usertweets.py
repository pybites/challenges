from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        # ...
        print("init method call here")
        self.handle = handle
        self.max_id = max_id

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

        # Redirect user to Twitter to authorize
        #redirect_user(auth.get_authorization_url())

        # Set access token
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Get access token
        #auth.get_access_token("verifier_value")

        # Construct the API instance
        self.api = tweepy.API(auth)
        #temp = self.api.user_timeline()
        #print("temp:", temp)

        self._tweets = list(self._get_tweets())
        print("Len Tweets:", len(self._tweets))
        self._save_tweets()
        self.output_file = DEST_DIR+'/'+self.handle+'.'+EXT

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        print("get_tweets method called here")

        ret_list = []
        #public_tweet = self.api.home_timeline()
        #public_tweet = self.api.user_timeline()
        #for tweet in public_tweet:
        #    print("tweet:", tweet.text)

        #for status in tweepy.Cursor(self.api.user_timeline).pages():
        counter = 0
        for status in self.api.user_timeline(id=self.handle, count=NUM_TWEETS+1, max_id=self.max_id):
            # process status here
            #print("status:", status)
            #print("id_str:", status.id_str)
            #print("created_at:", status.created_at)
            print(counter,"text:", status.text)
            counter += 1
            ret_list.append(Tweet(id_str=status.id_str, created_at=status.created_at, text=status.text))

            #temp = [l for l in status if l not in 'id_str']

        return ret_list
        pass

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows
        Save the tweets as data/<handle>.csv"""
        print("save_tweets method call here")

        with open(DEST_DIR+'/'+self.handle+'.'+EXT, 'w', newline='') as csvfile:
            tweetwriter = csv.writer(csvfile, delimiter=',')
            tweetwriter.writerow(['id_str', 'created_at', 'text'])
            tweetwriter.writerows(self._tweets)
            #for x in Tweet:
            #    print("x:", x)
            #    #tweetwriter.writerows(Tweet)
            #print("Tweet:", self._tweets)

        print("END")
        pass

    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)
        pass

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]
        pass


if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
    #for handle in ('jcastle13', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
