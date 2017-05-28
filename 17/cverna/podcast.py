#!/usr/bin/python3
# http://pybit.es/codechallenge17.html
import os
import sys
import sqlite3
import smtplib
from collections import namedtuple
from random import randint
from email.mime.text import MIMEText
# this module might save you time parsing feeds
import feedparser

FEED = 'https://www.podcastinit.com/feed/mp3/'

conn = sqlite3.connect('dbpodcast.sqlite')
db = conn.cursor()

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_account = os.environ.get('MAIL_ACCOUNT')
smtp_password = os.environ.get('MAIL_PASSWORD')
mailto = os.environ.get('MAILTO')

Episode = namedtuple('Episode', 'title url')


# Feed parsing
def parse_feed(feed=FEED):
    items = []
    feed = feedparser.parse(feed)
    for entry in feed['entries']:
        for link in entry['links']:
            if link['type'] == 'audio/mpeg':
                ep_data = Episode(title=entry['title'], url=link['href'])
                items.append(ep_data)
    return items


# Keep cache of feed in SQLite

def get_episodes_from_db(unplayed=False):
    if unplayed:
        db.execute("SELECT * FROM podcast WHERE played=0")
    else:
        db.execute("SELECT title FROM podcast")
    rows = db.fetchall()
    return rows


def add_new_episodes_to_db(episodes):
    old_episode = get_episodes_from_db()
    for episode in episodes:
        if (episode.title,) not in old_episode:
            db.execute("INSERT INTO podcast (title, url, played) VALUES ('{}', '{}', 0)".
                       format(episode.title, episode.url))
            conn.commit()


# Send out new episode and mark as complete

def get_random_episode():
    unplayed = get_episodes_from_db(unplayed=True)
    if len(unplayed) > 0:
        episode = randint(0, len(unplayed)-1)
        return unplayed[episode]


def mark_episode_done(episode):
    db.execute("UPDATE podcast SET played=1 WHERE title='{}'".format(episode[0]))
    conn.commit()


def mail_episode(episode):
    # could use os.environ to retrieve credentials
    smtp_server.ehlo()
    smtp_server.starttls()
    try:
        smtp_server.login(smtp_account, smtp_password)
    except smtplib.SMTPAuthenticationError:
        print('Could not login to the smtp server please check your username and password')
        sys.exit(1)
    msg = MIMEText('\nHi this week podcast is {} you can download it from here {}'.
                   format(episode[0], episode[1]))
    msg['Subject'] = 'My podcast of the week'
    msg['From'] = smtp_account
    msg['To'] = mailto
    smtp_server.send_message(msg)
    smtp_server.quit()

    mark_episode_done(episode)


def main():
    db.execute(
        'CREATE TABLE IF NOT EXISTS podcast (title TEXT PRIMARY_KEY, url TEXT, played INTEGER)')
    feed = parse_feed()
    add_new_episodes_to_db(feed)
    episode = get_random_episode()
    if episode is not None:
        mail_episode(episode)
        print('Podcast {} successfully sent !!'.format(episode[0]))


if __name__ == '__main__':
    main()
    conn.close()
