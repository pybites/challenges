import csv
import datetime
import unittest

from usertweets import UserTweets
from usertweets import NUM_TWEETS

DT = datetime.datetime(2017, 1, 13, 9, 0, 5)
HANDLE = 'pybites'
MAX_ID = '819831370113351680'
TWEETS = (
    """5 cool things you can do with itertools https://t.co/Nk4s3yL6zL #python""",
    """How to create a nice-looking HTML page of your #Kindle book highlights (notes) https://t.co/HKFK7inhUa #python""",
)
USER = UserTweets(HANDLE, max_id=MAX_ID)

def read_csv():
    with open(USER.output_file) as f:
        r = csv.reader(f)
        next(r, None)  # skip the headers
        return list(r) 

class TestUserTweets(unittest.TestCase):

    def test_num_tweets(self):
        self.assertEqual(len(USER), NUM_TWEETS)

    def test_first_tweet_returned_by_api(self):
        self.assertEqual(USER[0].id_str, MAX_ID)
        self.assertEqual(USER[0].created_at, DT)
        self.assertEqual(USER[0].text, TWEETS[0])

    def test_read_back_from_cached_csv(self):
        csv_tweets = read_csv()
        self.assertEqual(len(csv_tweets), NUM_TWEETS)
        self.assertEqual(csv_tweets[0][0], MAX_ID)
        self.assertEqual(csv_tweets[0][1], str(DT))
        self.assertEqual(csv_tweets[0][2], TWEETS[0])
        self.assertEqual(csv_tweets[-1][2], TWEETS[1])

if __name__ == "__main__":
    unittest.main()
