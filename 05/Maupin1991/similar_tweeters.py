from gensim import corpora, similarities, models
import sys
from user_tweets import UserTweets

N_TWEETS = 10  # number of tweets to compare
MIN_LEN = 3  # minimum length of a word to be considered
STOP_LIST = """for a of the and to in that from where this with your this have"""  # words to remove
NUM_TOPICS = 10  # number of topics to compare

def tokenize(texts):
    """
    Tokenizes the words in the tweets, filtering out stop words, URLs, digits,
    punctuation, words that only occur once or are less than 3 characters (and/or other noise ...)
    :param texts:    list of texts to tokenize
    :return:        list of tokens
    """
    # remove common words and tokenize
    stoplist = set(STOP_LIST.split())
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in texts]

    # remove words that appear only once, short words and
    # tag words from twitter
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    return [[token for token in text
             if frequency[token] > 5 and
             len(token) > MIN_LEN and
             not token.startswith("#") and
             not token.startswith("@")
             ] for text in texts]



def get_tweets(tw):
    """Returns all the tweets from a user"""
    return tw.text


def similar_tweeters(*users):
    """
    performs natural language analysis of different twitter users and returns
    a matrix with the similarity score between them
    :param users: usernames for the twitter API
    :return sims: similarity matrix. The score between user j and k (starting from zero) can be read at position
                  sims[j][k]
    """

    # get a list of user_tweets joined in a string, with space as separator
    users_list = [UserTweets(user) for user in users]
    tweets = list(" ".join(map(get_tweets, user)) for user in users_list)

    # get dictionary from all tweets from the specified users
    dictionary = corpora.Dictionary(tokenize(tweets))

    # get the vectors from the texts
    vecs = [dictionary.doc2bow(user_tw.lower().split()) for user_tw in tweets]

    # generate model for getting the main topics
    lsi = models.LsiModel(corpus=vecs, id2word=dictionary, num_topics=NUM_TOPICS)
    vec_lsi = lsi[vecs]

    # use cosine similarity for getting a similarity score
    # WARNING do not use this if corpus is big, since it will have to fit in ram

    # transform corpus to LSI space and index it
    index = similarities.MatrixSimilarity(lsi[vecs], num_features=len(dictionary))
    sims = index[vec_lsi]

    # return the similarity matrix
    return sims


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)
    user1, user2 = sys.argv[1:3]
    similarity_matrix = similar_tweeters(user1, user2)
    print(similarity_matrix[0][1])
