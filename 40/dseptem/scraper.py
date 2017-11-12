import json
import re
from twitterscraper import query_tweets
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def check_twit(tw_id):
    return es.exists(index='tweets', doc_type='tw', id=tw_id)


def create_json(tw):
    print(f'creating json for {tw.id}')
    tag_finder = re.compile('\B(#\w+)')
    data = {
        'text': tw.text,
        'date': str(tw.timestamp),
        'likes': tw.likes,
        'retweets': tw.retweets,
        'tags': [tag.group() for tag in tag_finder.finditer(tw.text)]
    }
    return json.dumps(data)


def post_json(j, t_id):
    print(f'posting json')
    if check_twit(id):
        return False
    res = es.create(index='tweets', doc_type='tw', body=j, id=t_id)
    try:
        return res['created']
    except IndexError:
        return False


def process_tweet(tw):
    exists = check_twit(tw.id)
    if exists:
        print(f'tweet {tw.id} already in db')
        return False
    print(f'tweet {tw.id} not in elastic, storing...')
    twj = create_json(tw)
    res = post_json(twj, tw.id)
    if not res:
        print('error storing tweet or tweet already in elastic')
        return False
    print(f'tweet stored')
    return True


def retrieve_tweets():
    retrieved = 0
    for tweet in query_tweets('from:python_tip exclude:replies'):
        res = process_tweet(tweet)
        if res:
            retrieved += 1
    print(f'Stored {retrieved} new tweets')


if __name__ == '__main__':
    retrieve_tweets()
