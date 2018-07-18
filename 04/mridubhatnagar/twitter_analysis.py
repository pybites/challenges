import config
import tweepy
import collections
import csv
import json


TWEET_DATA = collections.namedtuple('UserTweets', 'id_str created_at tweet_text')
TWEET_COUNT = 100




class UserTweets(object):
	"""
	Fetch Tweets from Users
	Timeline. Store retrieved 
	tweets in CSV file.
	"""


	def __init__(self, handle,max_id=None):

		self.twitter_handle = handle
		self._tweets = []
		self.get_tweets()
		self.save_tweets()

    
	def get_tweets(self):
		"""
		Fetches tweets from user 
		timeline
		"""
		data = api.user_timeline(self.twitter_handle, count=TWEET_COUNT)
		print(type(data))
		print(len(data))

		for tweet in data:
		
		    T = TWEET_DATA(tweet.id_str, tweet.created_at, tweet.text)
		    self._tweets.append(T)

		return self._tweets


	def save_tweets(self):
		"""
		Save tweets to a CSV file
		"""

		with open('data/some_handle.csv', 'a') as file:
			x = csv.writer(file, delimiter='\n')

			x.writerow(self._tweets)


	def __len__(self):
		"""
		Get length of the
		object
		"""
		
		return len(self._tweets)
    

	def __getitem__(self, position):
		"""
		Iterate over the object
		"""

		return self._tweets[position]


if __name__ == '__main__':

	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET_KEY)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
 
    # Creation of the actual interface, using authentication
	api = tweepy.API(auth)

	for twitter_handle in ('realpython', 'pybites'):
		# To fetch 100 tweets
	    user = UserTweets(twitter_handle)

	for data in user[:20]:
		print(data)


	print(len(user))



        

	

	

