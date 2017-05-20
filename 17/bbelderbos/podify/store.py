import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from podify.models import Base, Podcast
from podify.utils.utils import get_db_name

DB_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'databases'))

class PodStore:

    def __init__(self, feed, dropall=False):
        db = os.path.join(DB_DIR, get_db_name(feed))
        engine = create_engine('sqlite:///{}.db'.format(db))
        if dropall:
            Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_episodes_from_db(self):
        return [row.id for row in self.session.query(Podcast.id).all()]

    def add_new_episodes_to_db(self, new_episodes):
        records = [Podcast(id=ep.id, title=ep.title, link=ep.link, published=ep.published)
                for ep in new_episodes.values()]
        self.session.add_all(records)
        self.session.commit()

    def get_random_episode(self):
        return self.session.query(Podcast).filter(Podcast.done==False).order_by(func.random()).first()

    def mark_episode_done(self, episode):
        episode.done = True
        self.session.commit()

    def get_stats(self):
        status = dict(self.session.query(Podcast.done, func.count(Podcast.done)).group_by(Podcast.done).all())
        done = status.get(True, 0)
        total = sum(status.values())
        perc = done/total * 100
        return 'Podcast consumption stats: {:.1f}% done [{} of {}]'.format(perc, done, total)
