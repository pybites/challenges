import re
import sys
from collections import defaultdict

from usertweets import UserTweets
import nltk

nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, similarities, models

stop_words = set(stopwords.words('english'))


def clean_tweet(tweet):
    # removes #, @ and URL
    tweet = re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet)
    tweet = re.sub("RT[\s]+", "", tweet)
    tweet = re.sub("[0-9]+", "", tweet)
    tweet = ' '.join([w for w in tweet.split() if len(w) > 3])
    return tweet


def tokenize_tweet(tweet):
    return word_tokenize(tweet)


def filter_tweet(tokens):
    return [w for w in tokens if not w.lower() in stop_words]


def preprocess_tweets(handle, tweet_count=5):
    user_tweets = UserTweets(handle)
    superset_tokens = []
    for tw in user_tweets[:tweet_count]:
        tweeted_text = clean_tweet(tw.text)
        tokens_text = tokenize_tweet(tweeted_text)
        filtered_text = filter_tweet(tokens_text)

        # remove words that appear only once
        frequency = defaultdict(int)
        for token in filtered_text:
            frequency[token] += 1

        superset_tokens.append([token for token in filtered_text if frequency[token] > 1])
    return superset_tokens


def similar_tweeters(user1, user2):
    number_of_tweets = 5000
    user1_tweets_relevant_tokens = preprocess_tweets(user1, number_of_tweets)
    user2_tweets_relevant_tokens = preprocess_tweets(user2, number_of_tweets)
    # print(user1_out)
    dictionary = corpora.Dictionary(user1_tweets_relevant_tokens)
    corpus = [dictionary.doc2bow(text) for text in user1_tweets_relevant_tokens]
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    vec_lsi = [lsi[dictionary.doc2bow(text)] for text in user2_tweets_relevant_tokens]
    index = similarities.MatrixSimilarity(lsi[corpus])

    sims = [index[a] for a in vec_lsi]
    most_similar = [max(a) for a in sims]
    mean_similarity = sum(most_similar) / len(most_similar)

    print('------- Checking Twitter Handle Similarity --------')
    print(f'Similarity between {user1} and {user2}: {round(mean_similarity, 4) * 100}%')
    # user2_tweets = UserTweets(user2)
    # for tw in user2_tweets[:5]:
    #     print(tw.text)
    # print()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
