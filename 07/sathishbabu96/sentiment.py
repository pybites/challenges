import json
import re
import sys

from textblob import TextBlob


def read_json(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)


emoticons_str = r"""(?:
[:=;] # Eyes
[.oO\-]? # Nose
[\)\(DPB/\\] # Mouth
)
"""
regex_str = [
    emoticons_str,  # emoticons
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    """find all the words that match with the tokens regex pattern"""
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    """tokenize and lowercase them"""
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return " ".join(tokens)


def get_sentiment(tweets):
    num_tweets = len(tweets)
    sentiment = 0
    for tweet in tweets:
        tb = TextBlob(tweet)
        _sentiment = tb.sentiment.polarity
        sentiment += _sentiment
    return sentiment / num_tweets


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)
    input_file = sys.argv[1]
    tweets = read_json(input_file)
    processed_tweets = [preprocess(tweet) for tweet in tweets]
    sentiment = get_sentiment(processed_tweets)
    if sentiment > 0:
        print(f'Reviews are positive. Positivity score {sentiment:.2f}')
    else:
        print(f'Reviews are negative. Negativity score {sentiment:.2f}')
