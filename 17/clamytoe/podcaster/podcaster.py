import logging
import os
import random
import re
from sys import exit

import feedparser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from podcaster.models import Base, Episode, Pod
from podcaster.utils.utils import check_dir, format_date, format_duration, format_link


# setup some logging
check_dir('logs')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')

file_handler = logging.FileHandler('logs/podcaster.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Podcast(object):
    def __init__(self, rss):
        """Constructor requires the url to the rss feed"""
        logger.debug(f'Creating Podcast from feed: {rss}')
        self.rss = rss
        self.title = None
        self.subtitle = None
        self.link = None
        self.author = None
        self.email = None
        self.image = None
        self.summary = None
        self.published = None
        self.id = None
        self.episodes = []

        check_dir('db')
        engine = create_engine('sqlite:///db/pods_db.sqlite')
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def update(self):
        """Internal method for retrieving the rss feed"""
        logger.debug(f'Retrieving: {self.rss}')
        response = feedparser.parse(self.rss)

        if response.status == 200:
            self.title = response.feed.title
            self.subtitle = response.feed.subtitle
            self.link = response.feed.link
            self.author = response.feed.author_detail.name
            self.email = response.feed.author_detail.email
            self.image = response.feed.image.href
            self.summary = re.sub('\w(\s{2,})\w', '', response.feed.summary)
            self.published = format_date(response.feed.published_parsed)
            shows = response.entries
            logger.debug(f'Shows: {len(shows)}')

            try:
                logger.debug(f'Attempting to locate podcast feed in db: {self.rss}')
                pod = self.session.query(Pod).filter(Pod.rss == self.rss).one()
                self.id = pod.id
                logger.debug(f'Found Pod ID: {self.id}')

                if pod.published != self.published:
                    logger.debug('Published dates do not match!')
                    self._update_pod(self.published)
                    episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
                    new_shows = dict((k, shows[k]) for k in shows.keys() if k not in episodes)
                    logger.debug(f'Found {len(new_shows)} new shows')
                    self.add_new_episodes_to_db(new_shows)
                else:
                    logger.debug(f'Populating episodes from db')
                    episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
                    for episode in episodes:
                        if not episode.done:
                            self.episodes.append(episode.id)
            except NoResultFound:
                logger.debug('Podcast not found, adding it:')
                self._add_pod()
                self.add_new_episodes_to_db(shows)
        else:
            # TODO: Handle other return codes from server
            logger.error('There was a error retrieving the rss feed')
            exit(1)

    def _add_pod(self):
        """Add new podcast to the database"""
        logger.debug(f'Adding new podcast from {self.rss}')
        published = self.published
        pod = Pod(title=self.title, subtitle=self.subtitle, link=self.link, rss=self.rss, author=self.author,
                  email=self.email, image=self.image, summary=self.summary, published=published)
        self.session.add(pod)
        self.session.commit()
        self.id = pod.id

    def _update_pod(self, published, caught_up=False):
        """Updates the passed values on the database"""
        logger.debug(f'Updating podcast {self.id} with a new published date of: {published}')
        self.session.query(Pod).filter(Pod.rss == self.rss).update({'published': published, 'caught_up': caught_up})
        self.session.commit()

    def get_episode(self, episode):
        """Grabs an episode from the database"""
        logger.debug(f'User requested episode {episode}')
        try:
            epi = self.session.query(Episode).filter_by(id = episode, pod_id = self.id).one()
            logger.debug(f'Episode {episode}: {epi.title}')
            return epi
        except NoResultFound:
            logger.error(f'User requested episode {episode}, which was not valid for this podcast')
            print(f'Episode: {episode} is not a valid')
            print(self.episodes)

    def get_episodes_from_db(self):
        """Gets all episodes from the database"""
        logger.debug(f'Retrieving all episodes from the database for podcast {self.id}')
        episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
        return episodes

    def add_new_episodes_to_db(self, shows):
        """Add a new episode to the database"""
        logger.debug(f'Adding {len(shows)} to the database')
        for episode in shows:
            # remove extra parameters from file link if they exist
            file_link = format_link(episode.links[1].href)
            duration_time = format_duration(episode.itunes_duration)
            published = format_date(episode.published_parsed)

            show = Episode(pod_id=self.id, title=episode.title, file=file_link, duration=duration_time,
                           published=published, summary=re.sub('<.*?>', '', episode.summary))
            self.session.add(show)
            self.session.commit()
            self.episodes.append(show.id)
            logger.debug(f'Added: [{show.id}] {show.title}')

    def get_random_episode(self):
        """Retrieves a random show from the database"""
        episode = random.choice(self.episodes)
        return self.get_episode(episode)

    def mark_episode_done(self, episode):
        """Update an episode as done in the database"""
        logger.debug(f'Marking episode {episode} as completed')
        self.session.query(Episode).filter(Episode.id == episode).update({'done': True})
        self.session.commit()
        self.episodes.remove(episode)
        logger.debug(f'Does episodes contain {episode}: {episode in self.episodes}')

    def email_episode(self, episode):
        """Email the selected episode"""
        # could use os.environ to retrieve credentials
        logger.debug(f'Attempting to mail episode {episode}')
        pass

    def __repr__(self):
        return f'Podcast "{self.title}" with {len(self.episodes)} episodes>'
