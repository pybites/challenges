from collections import OrderedDict
from pytest import fixture
from podcaster import Podcast


@fixture
def feed_keys():
    # Responsible for only returning the test data
    return ['feed', 'status', 'version', 'encoding', 'bozo', 'headers', 'href', 'namespaces', 'entries']


@fixture
def parse_keys():
    # Responsible for only returning the test data
    return ['title', 'published', 'file', 'duration', 'summary']


def test_feed_info(feed_keys):
    """Tests the RSS feed for the podcast info"""

    rss = 'https://pythonbytes.fm/episodes/rss'
    feed_instance = Podcast(rss)
    response = feed_instance._info()

    assert isinstance(response, dict)
    assert isinstance(response['entries'], list)
    assert isinstance(response['headers'], dict)
    assert feed_instance.rss == 'https://pythonbytes.fm/episodes/rss', "The url should have been passed on creation"
    assert response.status == 200, "Should get a successful connection"
    assert response.version == 'rss20', "The RSS version should match"
    assert response.encoding == 'UTF-8', "The correct encoding should be returned"
    assert response.href == feed_instance.rss, "The rss entry passed into the object should be the same as href value"
    assert set(feed_keys).issubset(response.keys()), "All feed keys should be in the response"


def test_parse_feed(parse_keys):
    """Tests the parser for the correct info"""

    rss = 'https://pythonbytes.fm/episodes/rss'
    feed_instance = Podcast(rss)
    episodes = feed_instance.parse_feed()

    # check for details about the podcast
    assert feed_instance.title == 'Python Bytes'
    assert feed_instance.subtitle == 'Developer headlines delivered directly to your earbuds'
    assert feed_instance.link == 'http://pythonbytes.fm/'
    assert feed_instance.author == 'Michael Kennedy'
    assert feed_instance.email == 'mikeckennedy@gmail.com'
    assert 'Brian Okken' in feed_instance.content, "Co-Author should be in the content detail"


    # test for proer prasing
    assert isinstance(episodes, OrderedDict)
    assert isinstance(episodes[1], dict)
    assert episodes[1]['title'] == '#1 Intro to the show and pip 9 is out!'
    assert episodes[1]['published'] == 'Mon, 07 Nov 2016 00:00:00 -0800'
    assert episodes[1]['duration'] == '00:16:38'
    assert episodes[1]['file'] == 'https://pythonbytes.fm/episodes/download/1/intro-to-the-show-and-pip-9-is-out.mp3'
    assert set(parse_keys).issubset(episodes[1].keys()), "All parsed keys should be in the response"
