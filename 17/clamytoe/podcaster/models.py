from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pod(Base):
    __tablename__ = 'podcasts'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    subtitle = Column(String)
    link = Column(String)
    rss = Column(String)
    author = Column(String)
    email = Column(String)
    image = Column(String)
    summary = Column(String)
    added_on = Column(DateTime, default=datetime.now())
    published = Column(DateTime)
    episodes = relationship('Episode', order_by='Episode.id', 
                            back_populates='pod', 
                            cascade='all, delete, delete-orphan')
    complete = Column(Boolean, default=False)
    total_episodes = Column(Integer, default=0)
    played = Column(Integer, default=0)
    status = Column(String, default='0 %')

    def __repr__(self):
        return f'<Podcast (id={self.id}, title={self.title}, '\
               f'updated={self.published}, episodes={len(self.episodes)},' \
               f' status={self.status})>'


class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    pod_id = Column(Integer, ForeignKey('podcasts.id'))
    pod = relationship('Pod', back_populates='episodes')
    title = Column(String)
    file = Column(String)
    duration = Column(String)
    published = Column(DateTime)
    summary = Column(String)
    done = Column(Boolean, default=False)

    def __repr__(self):
        return f'<Episode (id={self.id}, pod_id={self.pod_id}, '\
               f'title={self.title}, duration={self.duration},' \
               f' done={self.done})>'
