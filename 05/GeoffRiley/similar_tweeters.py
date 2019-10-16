"""
PyBites challenge 05: https://codechalleng.es/challenges/5/
"""
import re
import string
import sys

from gensim import corpora, models, similarities
import nltk
from nltk.corpus import stopwords
from user_tweets import UserTweets

nltk.download('stopwords')
sw = set(stopwords.words('english'))

# exclusions:
#  1. Tags starting with '#'
#  2. email addresses containing '@'
#  3. web addresses containing 'http' or 'https'
#  4. URL indicators beginning '//'
#  5. numbers comprising one or more digits followed by an optional two alphas
exclusions = re.compile(r'^(#.*|.*@.*|.*https?|//.*|\d+([a-zA-Z]{2})?)$')
my_punct = ''.join(x for x in string.punctuation if x not in ['#', '@'])
trans = str.maketrans(my_punct, ' ' * len(my_punct))


def clean_words(usr: UserTweets) -> list:
    result = []
    for twitter in usr:
        for word in twitter.text.translate(trans).lower().split():
            if word not in sw and len(word) > 3 and not exclusions.match(word):
                result.append(word)
    return result


def similar_tweeters(user1, user2):
    tw1 = clean_words(UserTweets(user1))
    tw2 = clean_words(UserTweets(user2))
    dictionary = corpora.Dictionary([tw1, tw2])
    vector = [dictionary.doc2bow(tw1), dictionary.doc2bow(tw2)]
    lsi = models.LsiModel(vector, id2word=dictionary, num_topics=100)
    vec_lsi = lsi[vector]

    index = similarities.MatrixSimilarity(vec_lsi)
    sims = index[vec_lsi]

    print(f'{user1:>20}:{user2:<20}')
    for s in sims:
        print(f'{s[0]:>20}:{s[1]:<20}')

    most_similar = [max(x) for x in sims]
    average_sim = sum(most_similar) / len(most_similar)

    print(f'Similarity index: {round(average_sim * 100, 2)}%')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
