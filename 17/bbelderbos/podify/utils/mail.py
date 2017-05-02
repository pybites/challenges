import logging
import os
import sys

USER = os.environ.get('PODCAST_MAILER_USER') or sys.exit('need env mail user')
USER = os.environ.get('PODCAST_MAILER_PW') or sys.exit('need env mail pw')


def mail_episode(ep, stats):
    subject = 'Podcast for today: {}'.format(ep.title)
    msg = '{}\n\n{}'.format(ep.link, stats)
    logging.debug('Subject: {}'.format(subject))
    logging.debug('Message: {}'.format(msg))
    print('TODO: mail')
    # mail
