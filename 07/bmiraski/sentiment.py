"""Determine sentiment of 1000 tweets on a topic."""

import json
from nltk.corpus import stopwords
from string import ascii_letters
from string import digits
from string import punctuation
import sys
from textblob import TextBlob

stoplist = set(stopwords.words('english'))


def read_json(input_file):
    """Read in json input file."""
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)


def clean_tweets(tweets):
    """Clean the tweet words."""
    return _get_important_tweet_words(tweets)


def _get_important_tweet_words(tweets):
    """Return a list of important words in user's tweets."""
    for count, tweet in enumerate(tweets):
        tweet_words = tweet.split()
        # print(tweet_words)
        for word, value in enumerate(tweet_words):
            clean_word = ""
            for char in value:
                if char in punctuation:
                    continue
                elif char in digits:
                    continue
                elif char not in ascii_letters:
                    continue
                clean_word += char
            tweet_words[word] = clean_word
        for word, value in enumerate(tweet_words):
            if value.startswith('http') or value in stoplist or len(value) < 3:
                tweet_words[word] = ""
        tweet_words = (' '.join(tweet_words)).split()
        tweets[count] = ' '.join(tweet_words)
    return tweets


def sentiment(tweets):
    """Determine sentiment."""
    tw_count = 0
    total_sent = 0
    for tw in tweets:
        tw_count += 1
        tweet_text = TextBlob(tw)
        sent = tweet_text.sentiment.polarity
        print(sent)
        total_sent += sent
    return total_sent/tw_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)
    input_file = sys.argv[1]
    tweets = read_json(input_file)
    # for tw in tweets:
    #     print(dict(tw)['text'])
    tweet_text = [dict(tw)['text'] for tw in tweets]
    # print(tweet_text)
    clean_tw = clean_tweets(tweet_text)
    # print(clean_tw)
    sent = sentiment(clean_tw)
    if sent == 0:
        print('Sentiment is split evenly.')
    elif sent > 0:
        print(f'Sentiment is positive: {sent:.3f}')
    else:
        print(f'Sentiment is negative: {sent:.3f}')
