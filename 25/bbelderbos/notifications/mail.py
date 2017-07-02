from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys

from themoviedb import get_genres_cache

BASE_IMG_URL = 'http://image.tmdb.org/t/p/w92{}'
BASE_MOVIE_URL = 'https://www.themoviedb.org/{}/{}'
SUBJECT = 'Movies / Series Digest'
GENRES = get_genres_cache()

FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL')

if not FROM_MAIL or not TO_MAIL:
    print('set FROM_MAIL and TO_MAIL in env')
    sys.exit(1)

# TODO: retrieve director and actors
TEMPLATE = '''<h4><a href="{link}">{title}</a></h4>
              <p>Overview: {overview}
              <img src="{img}" style="float: right;"></p>
              <p>Genres: {genres} / (first) release: {release}</p>
              <hr>
            '''


def generate_mail_msg(items):
    output = []

    for kind in items:
        output.append('<h2>{}</h2>'.format(kind))

        for listing, entries in items[kind].items():
            output.append('<h3>{}</h3>'.format(listing))

            if not entries:
                output.append('No new items')
                continue

            for entry in sorted(entries,
                                key=lambda x: datetime.strptime(
                                              x.release_date, '%Y-%m-%d'),
                                reverse=True):

                img = BASE_IMG_URL.format(entry.poster)
                kind_for_url = kind.replace('movies', 'movie')
                url = BASE_MOVIE_URL.format(kind_for_url, entry.id)
                genres = ', '.join([GENRES.get(gen) for gen in entry.genres
                                    if GENRES.get(gen)])

                output.append(TEMPLATE.format(link=url,
                                              title=entry.title,
                                              overview=entry.overview,
                                              img=img,
                                              genres=genres,
                                              release=entry.release_date))

    return '\n'.join(output)


def mail_msg(content, recipients=TO_MAIL, subject=SUBJECT):
    if isinstance(recipients, list):
        recipients = ', '.join(recipients)

    sender = FROM_MAIL

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    part = MIMEText(content, 'html')
    msg.attach(part)

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
