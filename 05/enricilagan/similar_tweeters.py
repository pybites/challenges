import string
import sys
from user_tweets import UserTweets
import os
import urllib.request
from collections import defaultdict
from gensim import corpora, models, similarities

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
if not os.path.isfile(stopwords_file):
    urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)

with open(stopwords_file, encoding='utf-8') as f:
    stopwords = f.read()
    stopwords = stopwords.lower().split()

replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))


def similar_tweeters(user1, user2):
    u1 = UserTweets(user1)
    u2 = UserTweets(user2)
    texts1 = _get_items(u1)
    texts2 = _get_items(u2)

    dictionary = corpora.Dictionary(texts1)
    corpus = [dictionary.doc2bow(text) for text in texts1]
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    vec_lsi = [lsi[dictionary.doc2bow(text)] for text in texts2]
    index = similarities.MatrixSimilarity(lsi[corpus])

    sims = [index[a] for a in vec_lsi]
    most_similar = [max(a) for a in sims]
    mean_similarity = sum(most_similar)/len(most_similar)

    print('------- Checking Twitter Handle Similarity --------')
    print(f'Similarity between {user1} and {user2}: {round(mean_similarity,4)*100}%')


def _get_items(u, n=200):
    # filtering out stop words, URLs, digits, punctuation,
    # Tokenize the words in the tweets
    # words that only occur once or are less than 3 characters (and/or other noise ...)
    texts = [[word.translate(replace_punctuation).strip() for word in d.text.lower().split()
              if word not in stopwords] for d in u[:n]]

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[a for a in text if frequency[a] > 1 and not a.startswith('http')
              and not a.isdigit() and a != '' and len(a) > 3]
             for text in texts]

    return texts


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
