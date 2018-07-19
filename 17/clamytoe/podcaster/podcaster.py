import logging
import os

from random import choice
from re import sub
from sys import exit

import click
import feedparser


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from podcaster.models import Base, Episode, Pod
from podcaster.utils.utils import check_dir, format_date, 
from podcaster.utils.utils import format_duration, format_link

USER_HOME = os.path.expanduser('~')
PODCASTER_DIR = os.path.join(USER_HOME, '.podcaster')
LOGS_DIR = os.path.join(PODCASTER_DIR, 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'podcaster.log')
MUSIC_DIR = os.path.join(USER_HOME, 'Music')
EPISODES_DIR = os.path.join(MUSIC_DIR, 'Podcasts')
DATABASE = os.path.join(PODCASTER_DIR, 'podcaster_db.sqlite')

check_dir(PODCASTER_DIR)
check_dir(LOGS_DIR)

# setup some logging
LOGS = os.path.join(LOGS_DIR, LOG_FILE)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# uncomment these lines to see debug messages in the terminal
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)


class Podcast(object):
    def __init__(self, rss):
        """Constructor requires the url to the rss feed"""
        check_dir(PODCASTER_DIR)
        engine = create_engine(f'sqlite:///{DATABASE}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        logger.debug(f'Creating Podcast with feed: {rss}')
        self.id = None
        self.rss = rss
        self.title = None
        self.subtitle = None
        self.link = None
        self.author = None
        self.email = None
        self.image = None
        self.summary = None
        self.published = None
        self.episodes = []
        self.complete = False
        self.total_episodes = len(self.episodes)
        self.played = 0
        self.status = '0 %'

        podcasts = self.get_all_podcasts()
        for podcast in podcasts:
            if podcast.rss == self.rss:
                logger.debug('Found podcast in the database')
                self._update_from_db(podcast)

        if len(self.episodes) < 1 and self.rss is not None:
            self.update()

    def update(self):
        """Internal method for retrieving the rss feed"""
        if self.rss:
            click.secho('DOWNLOADING FEED:', blink=True, nl=False)
            click.secho(f'{self.rss}', bold=True)
            logger.debug(f'Retrieving: {self.rss}')
            response = feedparser.parse(self.rss)

            if response.status == 200:
                self.title = response.feed.title
                raw_sub = response.feed.subtitle
                subtitle = self._clean_up(raw_sub)
                self.subtitle = subtitle
                self.link = response.feed.link
                self.author = response.feed.author_detail.name
                self.email = response.feed.author_detail.email
                self.image = response.feed.image.href
                raw_sum = response.feed.summary
                summary = self._clean_up(raw_sum)
                self.summary = summary
                self.published = format_date(response.feed.published_parsed)
                shows = response.entries
                logger.debug(f'Shows Available: {len(shows)}')

                try:
                    logger.debug('Attempting to locate podcast feed in db:')
                    pod = self.session.query(Pod).filter(Pod.rss == self.rss).one()
                    self.id = pod.id
                    logger.debug(f'Found Pod ID: {self.id}')

                    if pod.published != self.published:
                        logger.debug('Feed is newer than what is in database, updating')
                        self._update_pod(self.published)
                        episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
                        new_shows = dict((k, shows[k]) for k in shows.keys() if k not in episodes)
                        logger.debug(f'Found {len(new_shows)} new shows')
                        self.add_new_episodes_to_db(new_shows)
                    else:
                        logger.debug(f'Populating episodes from db')
                        episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
                        if episodes:
                            self._update_status()
                        else:
                            logger.debug(f'Podcast {self.id} exists in database, but has no episodes. Adding them now')
                            self.add_new_episodes_to_db(shows)
                except NoResultFound:
                    logger.debug('Podcast not found, adding it:')
                    self._add_pod()
                    self.add_new_episodes_to_db(shows)
            else:
                # TODO: Handle other return codes from server
                logger.error('There was a error retrieving the rss feed')
                exit(1)
        else:
            logger.debug('Attempted to update dummy podcast object')
            click.echo('You can not update the dummy object')

    @staticmethod
    def _clean_up(block_text):
        """Takes the given block of text and cleans it up"""
        clean = sub('\w(\s{2,})\w', '', block_text)
        clean = sub(' +', ' ', clean)
        clean = sub('\n+ ', '\n', clean)
        return clean

    def _update_from_db(self, podcast):
        """Update podcast information from existing entries in the database"""
        logger.debug('Retriving values from the databse')
        self.id = podcast.id
        self.title = podcast.title
        self.subtitle = podcast.subtitle
        self.link = podcast.link
        self.author = podcast.author
        self.email = podcast.email
        self.image = podcast.image
        self.summary = podcast.summary
        self.published = podcast.published
        self.episodes = podcast.episodes
        self.complete = podcast.complete
        self.total_episodes = podcast.total_episodes
        self.played = podcast.played
        self.status = podcast.status
        self._update_status()

    def _add_pod(self):
        """Add new podcast to the database"""
        logger.debug(f'Adding new podcast from {self.rss}')
        published = self.published
        subtitle = self._clean_up(self.subtitle)
        summary = self._clean_up(self.summary)
        pod = Pod(title=self.title, subtitle=subtitle, link=self.link, 
                  rss=self.rss, author=self.author, email=self.email, 
                  image=self.image, summary=summary, published=published)
        self.session.add(pod)
        self.session.commit()
        self.id = pod.id

    def _update_pod(self, published):
        """Updates the passed values on the database"""
        logger.debug(f'Updating podcast {self.id} with a new published date of: {published}')
        self.session.query(Pod).filter(Pod.rss == self.rss).update({'published': published})
        self.session.commit()

    def _update_status(self):
        """Updates the status of the podcast"""
        logger.debug(f'Updating the status of podcast {self.id}')
        all_episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
        played_episodes = self.session.query(Episode).filter_by(pod_id=self.id, done=True).all()
        total = len(all_episodes)
        listened_to = len(played_episodes)
        percentage = int((listened_to / total) * 100 + 0.5)

        logger.debug('Updating the database with new values')
        # update current instance
        self.episodes = all_episodes
        self.total_episodes = total
        self.played = listened_to
        self.status = f'{percentage}%'
        self.complete = True if (total == listened_to) else False

        self.session.commit()

    def list_episodes(self):
        """Displays all of the episodes for the podcast"""
        print('Valid episodes:')
        for episode in self.episodes:
            played = 'Played' if episode.done else '      '
            click.secho(f' {played} ', fg='green', bg='black', nl=False)
            click.secho(f'[{episode.id:02d}]', fg='magenta', bg='black', 
                        nl=False)
            click.secho(': ', fg='green', bg='black', nl=False)
            click.secho(f'{episode.title}', fg='white', bg='black', nl=True)

    def get_episode(self, episode_id):
        """Grabs an episode from the database"""
        logger.debug(f'User requested episode {episode_id}')
        if isinstance(episode_id, int):
            try:
                epi = self.session.query(Episode).filter_by(id=episode_id, 
                      pod_id=self.id).one()
                logger.debug(f'Episode {epi.id}: {epi.title}')
                return epi
            except NoResultFound as e:
                logger.exception(f'User requested episode {episode_id}, which was not valid for this podcast')
                logger.exception(e)
                self.list_episodes()
        else:
            self.list_episodes()

    def get_episodes_from_db(self, pod_id=None):
        """Gets all unplayed episodes from the database"""
        logger.debug(f'Retrieving all episodes from the database')
        if pod_id:
            logger.debug(f'All episodes from Podcast {pod_id}')
            episodes = self.session.query(Episode).filter(Episode.pod_id == pod_id).all()
        else:
            logger.debug('From all from current podcast')
            episodes = self.session.query(Episode).filter(Episode.pod_id == self.id).all()
            self.total_episodes = len(episodes)

        return episodes

    def add_new_episodes_to_db(self, shows):
        """Add a new episode to the database"""
        logger.debug(f'Adding {len(shows)} to the database')

        with click.progressbar(shows, label="Adding episodes to database") as bar:
            for episode in bar:
                # remove extra parameters from file link if they exist
                file_link = format_link(episode.links[1].href)
                duration_time = format_duration(episode.itunes_duration)
                published = format_date(episode.published_parsed)

                show = Episode(pod_id=self.id, title=episode.title, 
                               file=file_link, duration=duration_time,
                               published=published, 
                               summary=sub('<.*?>', '', episode.summary))
                self.session.add(show)
                self.session.commit()
                logger.debug(f'Added: [{show.id}] {show.title}')

        self._update_status()

    def get_random_episode(self, pod_id=None):
        """Retrieves a random show from the database"""
        if self.rss:
            if not self.complete:
                if pod_id:
                    logger.debug(f'Retrieving a random episode for podcast {pod_id}')
                    episodes = self.get_episodes_from_db(pod_id)
                else:
                    episodes = [episode for episode in self.episodes if episode.done is False]

                episode = choice(episodes)
                return episode
            else:
                logger.debug('There are no more unplayed episodes')
                print('You have already played all of the episodes!')
                return None

    def mark_episode_done(self, episode):
        """Update an episode as done in the database"""
        logger.debug(f'Marking episode {episode.id} as completed')
        self.session.query(Episode).filter(Episode.id == episode.id).update({'done': True})
        self.session.commit()
        self._update_status()

    def get_all_podcasts(self):
        """Returns all available podcasts in the database"""
        podcasts = self.session.query(Pod).all()
        return podcasts

    def get_podcast(self, pod_id):
        """Retrieves the specified podcast from the database"""
        pod = self.session.query(Pod).filter(Pod.id == pod_id).one()
        podcast = Podcast(pod.rss)
        podcast.update()
        return podcast

    @staticmethod
    def download_episode(episode):
        """Download an episode"""
        check_dir(EPISODES_DIR)
        link = episode.file
        mp3 = link.split('/')[-1]
        mp3_path = os.path.join(EPISODES_DIR, mp3)
        cmd = f'wget --no-verbose --show-progress -c {link} -O {mp3_path}'

        # I tried doing this withing Python, but couldn't get a progress bar working
        os.system(cmd)

    @staticmethod
    def email_episode(episode):
        """Email the selected episode"""
        # TODO: Setup email handler
        # could use os.environ to retrieve credentials
        logger.debug(f'Attempting to mail episode {episode}')
        click.secho('Emailing episodes is not implemented yet', fg='red', 
                    bold=True)

    def __repr__(self):
        return f'<Podcast (id={self.id}, title={self.title}, '\
               f'updated={self.published}, episodes={len(self.episodes)},' \
               f' status={self.status})>'
