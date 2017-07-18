import os

import praw

DEFAULT_SUBREDDIT = 'learnpython'

reddit = praw.Reddit(client_id=os.environ.get('PRAW_CLIENT_ID'),
                     client_secret=os.environ.get('PRAW_CLIENT_SECRET'),
                     password=os.environ.get('PRAW_PASSWORD'),
                     user_agent='pybites_codechallenges by /u/bbelderbos',
                     username='bbelderbos')


def submit_to_reddit(post, subreddit=DEFAULT_SUBREDDIT):
    '''Submits post to subreddit'''
    title = post.title
    text = '{} - {}'.format(post.summary, post.url)

    return reddit.subreddit(subreddit).submit(title,
                                              selftext=text)
