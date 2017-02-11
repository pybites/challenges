import csv
import glob
import os
import re
from string import ascii_lowercase
import sys

from gensim import corpora, models, similarities
from nltk.corpus import stopwords

from tweet_dumper import get_all_tweets 

CSV = 'data/new/{}.csv'
IS_LINK_OBJ = re.compile(r'^(?:@|https?://)')
STOPWORDS = set(stopwords.words('english'))


def _is_ascii(w):
    return all(ord(c) < 128 for c in w)


def _strip_non_ascii(w):
    return ''.join([i for i in w if i in ascii_lowercase])


def _get_filename(u):
    return os.path.splitext(os.path.basename(u))[0]


def get_user_tokens(user):
    tweets_csv = CSV.format(user)
    if not os.path.isfile(tweets_csv):
        get_all_tweets(user)
    words = []
    with open(tweets_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for w in row['text'].lower().split():
                words.append(w)
    return tokenize_text(words)


def tokenize_text(words):
    words = [word for word in words if len(word) > 4 and word not in STOPWORDS]
    words = [word for word in words if _is_ascii(word)]
    words = [word for word in words if not IS_LINK_OBJ.search(word)]
    #words = [_strip_non_ascii(word) for word in words]
    return words


if __name__ == "__main__":

    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = 'bbelderbos'
    if len(sys.argv) > 2:
        diff_users = sys.argv[1:]
    else:
        diff_users = [i for i in glob.glob(CSV.format('*')) if user not in i]
        diff_users = [_get_filename(u) for u in diff_users]

    data = []
    for du in diff_users:
        data.append(get_user_tokens(du))
    dictionary = corpora.Dictionary(data)

    corpus = [dictionary.doc2bow(text) for text in data]
    lda = models.ldamodel.LdaModel(corpus, num_topics=5,
                                   id2word=dictionary, passes=15)

    index = similarities.MatrixSimilarity(lda[corpus])

    tokens = get_user_tokens(user)
    vec_bow = dictionary.doc2bow(tokens)
    vec_lda = lda[vec_bow]

    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    for i, sim in sims:
        print(diff_users[i], sim)
