# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Tweets analyzer script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from extractor import TweetsExtractor
from collections import OrderedDict


class TweetsAnalyzer():

    def __init__(self, extractor):
        """
        Constructor function using a TweetsExtractor
        object.
        """

        # Construct object:
        self.extractor = extractor
        self.data = None
        self.hashtags = {}

        return

    def analyze(self, user):
        """
        Analyzer function to gather all data from
        a TweetsExtractor object.
        """

        # Extract data from extractor:
        self.data = self.extractor.extract(user)

        # Construct hashtags dictionary:
        for entity in self.data['Entities']:
            if entity['hashtags']:
                for hashtag in entity['hashtags']:
                    if hashtag['text'] in self.hashtags.keys():
                        self.hashtags[hashtag['text']] += 1
                    else:
                        self.hashtags[hashtag['text']] = 1

        self.hashtags = OrderedDict(sorted(self.hashtags.items()))

        return

    def hashtags(self):
        """
        Function to return a dictionary containing all
        hashtags from extracte data.
        """

        return self.hashtags

    def top_hashtags(self, top=1e10):
        popular = sorted(self.hashtags.items(), key=lambda h: h[1], reverse=1)
        return popular[:top]

    def trending_tweets(self):
        """
        Utility funtion that returns the indices of
        the most popular tweets: the most liked and
        the most retweeted.
        """

        # We extract the tweet with more FAVs and more RTs:
        fav_max = max(self.data['Likes'])
        rt_max = max(self.data['RTs'])

        # Save the index of the first most liked and RT'd tweet:
        fav = self.data[self.data.Likes == fav_max].index[0]
        rt = self.data[self.data.RTs == rt_max].index[0]

        return fav, rt


if __name__ == '__main__':
    extractor = TweetsExtractor()
    analyzer = TweetsAnalyzer(extractor)
    analyzer.analyze("FerroRodolfo")
    print(analyzer.hashtags)
