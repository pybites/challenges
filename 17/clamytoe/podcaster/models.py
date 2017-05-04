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
    episodes = relationship('Episode', order_by='Episode.id', back_populates='pod',
                            cascade='all, delete, delete-orphan')
    caught_up = Column(Boolean, default=False)

    def __repr__(self):
        return f'<Podcast (id={id}, title={title}, updated={published}, caught_up={caught_up})>'


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
        return f'<Episode (id={id}, pod_id={pod_id}, title={title}, duration={duration}, done={done})>'
