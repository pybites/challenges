from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys

SUBJECT = 'New PyBites Code Challenge'
MAIL_MSG = '''Dear Pythonistas, our new code challenge is up:

{title}
{url}

Please take a moment to upvote it on reddit:
{submission}

Previous challenges:
https://pybit.es/pages/challenges.html'''

FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL').split()
if not FROM_MAIL or not TO_MAIL:
    print('Please set FROM_MAIL and TO_MAIL env vars')
    sys.exit(1)


def mail(recipients, msg_body, subject=SUBJECT, from_=FROM_MAIL, to=TO_MAIL):
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
