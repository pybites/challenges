import sys

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

import config as c

OUTPUT = 'data.json'

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(OUTPUT, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        
 
if __name__ == '__main__': 
    auth = OAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
    auth.set_access_token(c.ACCESS_TOKEN, c.ACCESS_SECRET)

    filter_on = ' '.join(sys.argv[1:])
    twitter_stream = Stream(auth, MyListener())
    print("Writing Tweets on term: {}".format(filter_on))
    twitter_stream.filter(track=[filter_on])
