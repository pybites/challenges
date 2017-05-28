import os
import sys

from podify.models import Podcast
from podify.store import PodStore
from podify.utils.feed import parse_feed
 
expected = 111
feed = 'https://talkpython.fm/episodes/rss'
pod = PodStore(feed, dropall=True)

feed_rss = 'talkpython.rss'
with open(feed_rss) as f:
    feed_content = f.read()

feed_output = parse_feed(feed_content)
assert len(feed_output) == expected

ids_in_db = pod.get_episodes_from_db()
assert len(ids_in_db) == 0

new_episodes = dict((k, feed_output[k]) 
		    for k in feed_output.keys() 
		    if k not in ids_in_db)

assert len(new_episodes) == expected

pod.add_new_episodes_to_db(new_episodes)
ids_in_db = pod.get_episodes_from_db()

assert len(ids_in_db) == expected

i = 0
stats = start_stat = None
while True:
    ep = pod.get_random_episode()
    if ep:
        pod.mark_episode_done(ep)
        stats = pod.get_stats()
        if i == 0:
            start_stat = stats
        i += 1
    else:
        break

assert i == expected
assert start_stat == 'Podcast consumption stats: 0.9% done [1 of {0}]'.format(expected)
assert stats == 'Podcast consumption stats: 100.0% done [{0} of {0}]'.format(expected)

print('Tests passed')
