import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

URL = "https://www.spreaker.com/show/3276901/episodes/feed"

class Podcast:
    def __init__(self, url=URL):
        self.feed = feedparser.parse(url)

    def latest_feed_data(self):
        items = self.feed.entries
        title = items[0].title
        link = items[0].link
        description = items[0].description
        date = items[0].published
        author = items[0].author
        data = {
            "title": title,
            "link": link,
            "description": description,
            "date": date,
            "author": author
        }
        return data

    def notify(self, data):
        msg = MIMEMultipart()
        msg["From"] = os.getenv("GMAIL_ACCOUNT")
        msg["To"] = os.getenv("EMAIL_DST")
        msg["Subject"] = "Feed available"
        body = f"""New feed:
        title: {data['title']}
        description: {data['description']}
        date: {data['date']}
        resource: {data['resource']}"""

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        print("Loggin to gmail server...")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(os.getenv("GMAIL_ACCOUNT"),os.getenv("GMAIL_PASS"))
        s.sendmail(os.getenv("GMAIL_ACCOUNT"),os.getenv("EMAIL_DST"),text)
        s.quit()

