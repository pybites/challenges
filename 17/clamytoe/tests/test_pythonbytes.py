from collections import OrderedDict
from pytest import fixture
from podcaster import Podcast


@fixture
def feed_keys():
    # Responsible for only returning the test data
    return ['title', 'published', 'published_parsed', 'file', 'duration', 'summary']


def test_feed_update(feed_keys):
    """Tests the RSS feed for the podcast info"""

    # rgso = 'https://audioboom.com/channels/4567086.rss'
    # talk = 'https://talkpython.fm/episodes/rss'
    pythonbytes = 'https://pythonbytes.fm/episodes/rss'
    feed_instance = Podcast(pythonbytes)

    assert set(feed_keys).issubset(feed_instance.episodes[1].keys()), "All feed keys should be in the response"

    # check for details about the podcast
    assert feed_instance.title == 'Python Bytes'
    assert feed_instance.subtitle == 'Developer headlines delivered directly to your earbuds'
    assert feed_instance.link == 'http://pythonbytes.fm/'
    assert feed_instance.author == 'Michael Kennedy'
    assert feed_instance.email == 'mikeckennedy@gmail.com'

    # # check for proper episode parsing
    assert isinstance(feed_instance.episodes, OrderedDict)
    assert feed_instance.rss == 'https://pythonbytes.fm/episodes/rss', "The url should have been passed on creation"
    assert feed_instance.episodes[1]['title'] == '#1 Intro to the show and pip 9 is out!'
    assert feed_instance.episodes[1]['published'] == 'Mon, 07 Nov 2016 00:00:00 -0800'
    assert feed_instance.episodes[1]['duration'] == '00:16:38'
    assert feed_instance.episodes[1]['file'] == \
           'https://pythonbytes.fm/episodes/download/1/intro-to-the-show-and-pip-9-is-out.mp3'
