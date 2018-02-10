# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets extractor script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# We import our access keys:
from credentials import *    # This will allow us to use the keys as variables
import pandas as pd
import tweepy as tw


class TweetsExtractor():

    def __init__(self):
        """
        Constructor function to setup the Twitter's API
        with our access keys provided.
        """

        # Authentication and access using keys:
        auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication:
        api = tw.API(auth)
        self.extractor = api
        return

    def extract(self, user):
        """
        Function to extract latest 200 tweets from a
        user provided.
        """

        # We create a tweet list as follows:
        tweets = self.extractor.user_timeline(
                    screen_name=user,
                    count=200,
                    tweet_mode='extended')

        # Print number of tweets extracted:
        print("Number of tweets extracted: {}.\n".format(len(tweets)))

        # We prepare data to create a dataframe:
        data = [[tw.full_text, len(tw.full_text), tw.id, tw.created_at,
                tw.source, tw.favorite_count, tw.retweet_count,
                tw.entities] for tw in tweets]
        columns = ['Tweets', 'len', 'ID', 'Date', 'Source',
                   'Likes', 'RTs', 'Entities']

        # We create a dataframe:
        dataframe = pd.DataFrame(data=data, columns=columns)

        return dataframe


if __name__ == '__main__':
    extractor = TweetsExtractor()
    data = extractor.extract("FerroRodolfo")
    print(data.head(5))
