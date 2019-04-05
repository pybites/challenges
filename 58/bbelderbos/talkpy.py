from collections import namedtuple
import sqlite3

import feedparser
import requests

TALKPY_FEED = 'https://talkpython.fm/episodes/rss'
TRANSCRIPT_URL = ('https://raw.githubusercontent.com/mikeckennedy/'
                  'talk-python-transcripts/master/transcripts/{}.txt')
EPISODE_LINK = '/mikeckennedy/talk-python-transcripts/blob/master/transcripts/'
TALKPY_DB = 'talkpy.db'
HTML_OUTPUT = 'talkpy.html'

Episode = namedtuple('Episode', 'number title description transcript')

conn = sqlite3.connect(TALKPY_DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def _parse_transcript_link(episode_id):
    """
    Grabs talkpy transcript for an episode id.
    Returns transcript if request successfull, otherwise an empty string.
    """
    # transcript files are 3 digit
    # see here a nice way to convert a number in 3 digits using f-strings:
    # https://github.com/pybites/challenges/pull/431
    number = f'{episode_id:0>3}'
    transcript = TRANSCRIPT_URL.format(number)
    resp = requests.get(transcript)
    return resp.content if resp.status_code == 200 else ''


def get_podcast_episodes(feed=TALKPY_FEED):
    """
    Parses Talk Python RSS feed returning a generator of Episode
    named tuples
    """
    feed = feedparser.parse(feed)
    for entry in feed['entries']:
        episode_id = entry.itunes_episode
        transcript = _parse_transcript_link(episode_id)
        yield Episode(number=episode_id,
                      title=entry.title,
                      description=entry.description,
                      transcript=transcript)


def create_table():
    """
    Create episodes database table using sqlite3.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS episodes (
        number integer,
        title text,
        description text,
        transcript text
    );
    """
    cur.execute(create_table_sql)
    conn.commit()


def insert_data(entries):
    """
    Inserts Talk Python Episode namedtuples in the episodes table.
    """
    # really neat it 'understands' namedtuples!
    insert_sql = "INSERT INTO episodes VALUES (?, ?, ?, ?)"
    cur.executemany(insert_sql, entries)
    conn.commit()


def output_episodes_html():
    """
    Retrieves all episodes from the DB and generates an HTML file.
    """
    sql = "SELECT * FROM episodes ORDER BY number ASC"
    cur.execute(sql)
    rows = cur.fetchall()

    output = []
    for row in rows:
        if isinstance(row['transcript'], bytes):
            transcript = row['transcript'].decode("utf-8", "ignore")
        else:
            transcript = row['transcript']

        output.append(f"<h1>Episode {row['title']}</h1>")  # contains number
        output.append(f"<h2>Description</h2>")
        output.append(row['description'])
        output.append(f"<h2>Transcript</h2>")
        output.append(transcript.replace('\n', '<br>'))
        output.append('<br><hr><br><br>')

    with open(HTML_OUTPUT, 'w') as f:
        f.writelines(output)


if __name__ == "__main__":
    create_table()
    insert_data(get_podcast_episodes())
    output_episodes_html()
