import argparse
import logging

from podify.models import Podcast
from podify.store import PodStore
from podify.utils.feed import parse_feed
from podify.utils.mail import mail_episode

DEFAULT_FEED = 'https://talkpython.fm/episodes/rss'

parser = argparse.ArgumentParser()
parser.add_argument('--feed', help='Podcast feed to parse')
args = parser.parse_args()

if args.feed:
    feed = args.feed
else:
    feed = DEFAULT_FEED

pod = PodStore(feed)

feed_output = parse_feed(feed)
ids_in_db = pod.get_episodes_from_db()

new_episodes = dict((k, feed_output[k]) 
		    for k in feed_output.keys() 
		    if k not in ids_in_db)

logging.debug('adding {} new episodes'.format(len(new_episodes)))
pod.add_new_episodes_to_db(new_episodes)

ep = pod.get_random_episode()
if not ep:
    logging.debug('no unplayed episode, no email')
else:
    pod.mark_episode_done(ep)
    stats = pod.get_stats()
    mail_episode(ep, stats)
