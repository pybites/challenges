import smtplib
from email.mime.text import MIMEText
import configparser

config = configparser.ConfigParser()
config.read("setting.ini")


class Mailer(object):

    def __init__(self, from_addr, to_addr):
        self.FROM_ADDR = from_addr
        self.TO_ADDR = to_addr

    def send(self, title, message):
        msg = MIMEText(message)
        msg['Subject'] = title
        msg['From'] = self.FROM_ADDR
        msg['To'] = self.TO_ADDR
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls()
        s.login(config['gmail']['user'], config['gmail']['key'])
        s.sendmail(
            self.FROM_ADDR,
            [self.TO_ADDR],
            msg.as_string(),
        )
        s.close()
