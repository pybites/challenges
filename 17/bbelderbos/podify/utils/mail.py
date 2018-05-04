from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
import smtplib
import sys

USER = os.environ.get('PODCAST_MAILER_USER') or sys.exit('need env mail user')


def mail_episode(ep, stats):
    subject = 'Podcast for today: {}'.format(ep.title)
    body = '{}\n\n{}'.format(ep.link, stats)
    
    logging.debug('Subject: {}'.format(subject))
    logging.debug('Message: {}'.format(body))

    to_emails = [USER]
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = USER
    msg['To'] = ", ".join(to_emails) 

    try:
        s = smtplib.SMTP('localhost')
        s.sendmail(USER, to_emails, msg.as_string())
        s.quit()
        logging.debug('Email sent')
    except Exception as exc:
        logging.error('Error sending email: {}'.format(exc))


if __name__ == '__main__':
    from collections import namedtuple

    Episode = namedtuple('Episode', 'title link')

    ep = Episode(title='new episode', link='http://somelink.com')
    stats = '10% done [1 out of 10]'

    mail_episode(ep, stats)
