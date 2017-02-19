####
#
# Twitter API querying, adapted from Joel Grus' great Data Science intro book
# https://github.com/joelgrus/data-science-from-scratch/blob/master/code-python3/getting_data.py
#
####
import json
import sys
import time

from twython import TwythonStreamer

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

MAX_TWEETS = 1000
OUTPUT = 'data_{}.json'.format(int(time.time()))


class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""
    count = 0

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            print(data)
            with open(OUTPUT, 'a') as f:
                f.write(json.dumps(data) + '\n')
            self.count += 1

        # stop when we've collected enough
        if self.count >= MAX_TWEETS:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


if __name__ == "__main__":
    keywords_and = ' '.join(sys.argv[1:])

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_SECRET)

    stream.statuses.filter(track=keywords_and)
