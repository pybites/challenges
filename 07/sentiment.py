from collections import defaultdict
import json
import sys

from textblob import TextBlob


def get_tweets(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)


def get_sentiment(polarity):
    if polarity < 0:
        return "negative"
    elif polarity == 0:
        return "neutral"
    else:
        return "positive"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)

    input_file = sys.argv[1]

    tweets = get_tweets(input_file)

    sentiments = defaultdict(set)

    for tw in tweets:
        text = dict(tw)['text'].lower()
        blob = TextBlob(text)
        sent = get_sentiment(blob.sentiment.polarity)
        sentiments[sent].add(text)

    total = sum(len(i) for i in sentiments.values())

    perc_pos = len(sentiments["positive"]) / total * 100
    perc_neg = len(sentiments["negative"]) / total * 100
    perc_neu = len(sentiments["neutral"]) / total * 100

    print("Analyzed {} tweets".format(total))
    print("Positive: {:.2f}%".format(perc_pos))
    print("Negative: {:.2f}%".format(perc_neg))
    print("Neutral: {:.2f}%".format(perc_neu))
