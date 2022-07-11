# Create your db here.
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(String, primary_key=True)
    text = Column(String)
    user_name = Column(String)
    user_email = Column(String)
    # created_at = DateTimeField()
    favorite_count = Column(Integer)
    retweet_count = Column(Integer)
    
    def __repr__(self):
        return "<Text: {}>".format(self.text)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})