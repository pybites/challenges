from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys

SUBJECT = 'New PyBites Code Challenge'
MAIL_MSG = '''<p>Dear Pythonistas, our new code challenge is up:</p>

<p><strong>{title}</strong><br>
<a href="{url}">{url}</a></p>

<p>Please take a moment to upvote it on reddit: <br>
<a href="{submission}">{submission}</a></p>

<p>Previous challenges:<br>
<a href="https://pybit.es/pages/challenges.html">https://pybit.es/pages/challenges.html</a></p>'''

FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL').split()
if not FROM_MAIL or not TO_MAIL:
    print('Please set FROM_MAIL and TO_MAIL env vars')
    sys.exit(1)

RECIPIENTS_LIST = 'challenge_user_emails.txt'
if not os.path.isfile(RECIPIENTS_LIST):
    print('please add recipient emails to {}'.format(RECIPIENTS_LIST))
    sys.exit(2)


def get_emails():
    with open(RECIPIENTS_LIST) as f:
        return [line.strip() for line in f.readlines() if '@' in line]


def mail(msg_body,
         recipients=None, subject=SUBJECT,
         from_=FROM_MAIL, to=TO_MAIL):

    if recipients is None:
        recipients = _get_emails()

    if not isinstance(recipients, list):
        raise TypeError('Except a list of recipients')

    bcc = recipients

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_
    msg['To'] = ', '.join(to)

    part = MIMEText(msg_body, 'html')
    msg.attach(part)

    s = smtplib.SMTP('localhost')
    s.sendmail(from_, to + bcc, msg.as_string())
    s.quit()
