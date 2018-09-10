import re
import sys

from feed import get_latest_feed_entry
from mail import MAIL_MSG, get_emails, mail
from reddit import submit_to_reddit

CODE_CHALLENGE_URL = re.compile(r'.*/codechallenge\d+\.html$')

post = get_latest_feed_entry(CODE_CHALLENGE_URL)
if not post:
    print('No recent code challenge found')
    sys.exit(1)

print('Retrieved last challenge: {}'.format(post))

try:
    submission = submit_to_reddit(post)
    submission_link = submission.shortlink
    print('Posted to reddit: {}'.format(submission_link))
except Exception as exc:
    print('Error posting to reddit, exception: {}'.format(exc))
    sys.exit(2)

msg_body = MAIL_MSG.format(title=post.title,
                           url=post.url,
                           submission=submission_link)

try:
    recipients = get_emails()
    mail(msg_body, recipients=recipients)
    print('Emailed challenge out to: {}'.format(recipients))
except Exception as exc:
    print('Error sending email, exception {}'.format(exc))
    sys.exit(3)
