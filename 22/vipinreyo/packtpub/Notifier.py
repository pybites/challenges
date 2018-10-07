import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notifier:
    """
    Notifier class for sending notifications.
    Currently implemented mail (with dummy sender and recipient mails)
    """
    GOOGLE_APP_PASS_CODE = None
    A_LINK = 'https://www.packtpub.com/packt/offers/free-learning?utm_source=Pybonacci&utm_medium=referral&utm_' \
             'campaign=FreeLearning2017CharityReferrals'

    def __init__(self):
        pass

    def send_notification_by_mail(self, book_details):
        self.GOOGLE_APP_PASS_CODE = os.getenv("GOOGLE_APP_PASS_CODE")

        self.from_email = 'sender@gmail.com'
        self.to_mail = 'recipient@gmail.com'

        self.msg = MIMEMultipart()
        self.msg['From'] = self.from_email
        self.msg['To'] = self.to_mail
        self.msg['Subject'] = 'PacktPub free book notification mail.'

        template = '<div>Title: {}</div>' \
                   '<div>{}</div>' \
                   '<div>Time left: {}</div>' \
                   '<hr>' \
                   '<img src=\'{}\'/>' \
                   '<hr>' \
            .format(book_details['title'], book_details['description'], book_details['time_left'],
                    book_details['cover'], self.A_LINK)

        self.body = template

        self.msg.attach(MIMEText(self.body, 'html'))

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login('sender@gmail.com', GOOGLE_APP_PASSCODE)

        text = self.msg.as_string()
        smtp_server.sendmail(self.from_email, self.to_email, text)
        smtp_server.quit()

        print('Email sent successfully...')
