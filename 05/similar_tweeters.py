from collections import Counter
import csv
import glob
import itertools
import os
import re
from string import ascii_lowercase
import sys

from gensim import corpora, models, matutils, similarities
from nltk.corpus import stopwords

CSV = 'data/{}.csv'
DB = 'twitter.dict'
IS_LINK_OBJ = re.compile(r'^(?:@|https?://)')
STOPWORDS = set(stopwords.words('english'))
IS_ASCII = lambda w: all(ord(c) < 128 for c in w)
STRIP_NON_ASCII = lambda w: ''.join([i for i in w if i in ascii_lowercase])

def similar_tweeters(*users):
    pass

def get_user_tokens(user):
    tweets_csv = CSV.format(user)
    words = []
    with open(tweets_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for w in row['text'].lower().split():
                words.append(w)
    return tokenize_text(words)
   
def tokenize_text(words):
    words = [word for word in words if len(word) > 4]
    words = [word for word in words if IS_ASCII(word)]
    words = [word for word in words if not IS_LINK_OBJ.search(word)]
    words = [word for word in words if word not in STOPWORDS]
    words = [STRIP_NON_ASCII(word) for word in words]
    return words


if __name__ == "__main__":

    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = 'bbelderbos'
    if len(sys.argv) > 2:
        diff_users = sys.argv[1:]
    else: 
        diff_users = [i for i in glob.glob(CSV.format('*')) if not user in i]
        diff_users = [os.path.splitext(os.path.basename(u))[0] for u in diff_users]
    
    data = []
    for du in diff_users:
        data.append(get_user_tokens(du))
    dictionary = corpora.Dictionary(data)
    
    corpus = [dictionary.doc2bow(text) for text in data]
    lda = models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

    index = similarities.MatrixSimilarity(lda[corpus])

    tokens = get_user_tokens(user)
    vec_bow = dictionary.doc2bow(tokens)
    vec_lda = lda[vec_bow]

    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    for i, sim in sims:
        print(diff_users[i], sim)
