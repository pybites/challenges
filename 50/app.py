import time

from flask import render_template, request, Flask

DEFAULT_BANNER = 'https://pbs.twimg.com/media/DZsKAs9W4AAEdpO.jpg:large'
DEFAULT_GREETING = 'I wish your a Happy Easter'
MSG = '''<p>Hey {name}, {greeting}!</p>
<p>Enjoy and keep calm and code in Python!</p>
<img width="400px;" src="{banner}" alt="nice Easter banner">
'''
TIMEOUT = 1

app = Flask(__name__)


def _emails_users(emails, banner, message):
    emails_done = {}
    for email in emails:
        # just printing message, bonus challenge: make it work with Sendgrid
        name = email.split('@')[0]  # for demo purposes
        mail_body = MSG.format(name=name,
                               greeting=message or DEFAULT_GREETING,
                               banner=banner,
                               message=message)

        emails_done[email] = mail_body

        # simulate some heavy processing
        time.sleep(TIMEOUT)

    return emails_done


@app.route('/', methods=['GET', 'POST'])
def login():
    banner = emails = message = emails_done = None

    if request.method == 'POST':
        banner = request.form.get('url') or DEFAULT_BANNER
        emails = [email.strip() for email in
                  request.form.get('emails').split(',')]
        message = request.form.get('message')

        emails_done = _emails_users(emails, banner, message).items()

    return render_template("index.html",
                           default_banner=DEFAULT_BANNER,
                           banner=banner or '',
                           emails=emails and ', '.join(emails) or '',
                           message=message or '',
                           emails_done=emails_done)


if __name__ == "__main__":
    app.run(debug=True)
