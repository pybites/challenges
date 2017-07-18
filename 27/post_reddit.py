from collections import namedtuple
from datetime import datetime, timedelta
from time import mktime
import os
import re
import sys

import feedparser
import praw

from mail import MAIL_MSG, mail

CODE_CHALLENGE_URL = re.compile(r'.*/codechallenge\d+\.html$')
DEFAULT_SUBREDDIT = 'learnpython'
DEFAULT_FEED = 'https://pybit.es/feeds/all.rss.xml'
DEFAULT_LOOK_DAYS_BACK = datetime.now() - timedelta(days=7)  # 1

Post = namedtuple('Post', 'title url summary')

reddit = praw.Reddit(client_id=os.environ.get('PRAW_CLIENT_ID'),
                     client_secret=os.environ.get('PRAW_CLIENT_SECRET'),
                     password=os.environ.get('PRAW_PASSWORD'),
                     user_agent='pybites_codechallenges by /u/bbelderbos',
                     username='bbelderbos')


def get_latest_feed_entry(url_match, feed=DEFAULT_FEED,
                          go_back_dt=DEFAULT_LOOK_DAYS_BACK):
    '''Returns most recent feed entry matching url_match regex'''
    for entry in feedparser.parse(feed)['entries']:
        title = entry['title']
        url = entry['link']

        summary_html = entry.get('summary', 'No summary available')
        summary_text = re.sub('<[^<]+?>', '', summary_html)

        published = entry['published_parsed']
        dt = datetime.fromtimestamp(mktime(published))

        if dt < go_back_dt:
            continue

        if not url_match.match(url):
            continue

        return Post(title=title,
                    url=url,
                    summary=summary_text)


def submit_to_reddit(post, subreddit=DEFAULT_SUBREDDIT):
    '''Submits post to subreddit'''
    title = post.title
    text = '{} - {}'.format(post.summary, post.url)

    reddit.subreddit(subreddit).submit(title, selftext=text)


if __name__ == '__main__':
    post = get_latest_feed_entry(CODE_CHALLENGE_URL)
    print('Retrieved last challenge: {}'.format(post))

    try:
        submission = submit_to_reddit(post)
        print('Posted to reddit: {}'.format(submission.url))
    except Exception as exc:
        print('Error posting to reddit, exception: {}'.format(exc))
        sys.exit(1)

    if len(sys.argv) < 2:
        print('No notification emails given from cli, done')
        sys.exit(2)

    msg_body = MAIL_MSG.format(title=post.title,
                               link=post.url,
                               submission=submission.url)

    try:
        recipients = sys.argv[1:]
        mail(recipients, msg_body)
        print('Emailed challenge out to: {}'.format(recipients))
    except Exception as exc:
        print('Error sending email, exception {}'.format(exc))
        sys.exit(3)
