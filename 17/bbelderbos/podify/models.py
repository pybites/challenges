from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Podcast(Base):
    __tablename__ = 'podcasts'
    id = Column('id', String(), primary_key=True)
    title = Column('title', String(), index=True)
    link = Column('link', String())
    published = Column('published', DateTime())
    done = Column('done', Boolean(), default=False)
    created_on = Column('created_on', DateTime(), default=datetime.now)
    updated_on = Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<Podcast(id='%s', title='%s', link='%s', published='%s', done='%s')>" \
               % (self.id, self.title, self.link, self.published, self.done)
