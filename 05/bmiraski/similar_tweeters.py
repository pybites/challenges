"""Compare tweet similarity from two users."""

from nltk.corpus import stopwords
import spacy
from string import ascii_lowercase
from string import digits
from string import punctuation
import sys
import usertweets


stoplist = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_md')


def similar_tweeters(user1, user2):
    """Output similarity value for two different users based on 200 tweets."""
    u1 = usertweets.UserTweets(user1)
    u2 = usertweets.UserTweets(user2)

    tt_u1 = " ".join(_word_set(
                     _remove_solo_words(_get_important_tweet_words(u1))))
    tt_u2 = " ".join(_word_set(
                     _remove_solo_words(_get_important_tweet_words(u2))))

    doc1 = nlp(tt_u1)
    doc2 = nlp(tt_u2)

    sim = doc1.similarity(doc2)

    print(sim)


def _get_important_tweet_words(user):
    """Return a list of important words in user's tweets."""
    tt = [[word for word in tweet.text.lower().split()]
          for tweet in user._tweets]
    for tweet in tt:
        for word, value in enumerate(tweet):
            clean_word = ""
            for char in value:
                if char in punctuation:
                    continue
                elif char in digits:
                    continue
                elif char not in ascii_lowercase:
                    continue
                clean_word += char
            tweet[word] = clean_word
    return [[word for word in tweet if not word.startswith('http') and
            word not in stoplist and len(word) >= 3]
            for tweet in tt]


def _remove_solo_words(tt):
    """Remove words occurring once in the array."""
    from collections import defaultdict
    frequency = defaultdict(int)
    for tweet in tt:
        for token in tweet:
            frequency[token] += 1
    return [[token for token in tweet if frequency[token] > 1]
            for tweet in tt]


def _word_set(tt):
    """Return a single list of all the words from array."""
    words = []
    for tweet in tt:
        for word in tweet:
            words.append(word)
    return words


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
