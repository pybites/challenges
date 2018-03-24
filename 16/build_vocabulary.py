import os
import requests
import json
import datetime
import smtplib
import logging
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG)


def fetch_response(url=None):
    """
    A GET request call is done on
    wordOftheDay endpoint in 
    wordlink API
    """

    response = requests.get(url)
    byte_response = response.content
    unicode_response = byte_response.decode("utf-8")
    logging.info("JSON response is fetched")
    parse_response(unicode_response)


def parse_response(response):
    """
    Returned response is 
    parsed and word of the day.
    origin, date, usage, meaning,
    part of speech and source are
    retrieved respectively.
    """
    
    json_response = json.loads(response)
    word_of_the_day = json_response["word"]
    origin = json_response["note"]
    date = json_response["publishDate"]
    usage = json_response["examples"][0]["text"]
    meaning = json_response["definitions"][0]["text"]
    part_of_speech = json_response["definitions"][0]["partOfSpeech"]
    source = json_response["definitions"][0]["source"]
    logging.info("Parsed JSON response")
    format_response(word_of_the_day, origin, date, usage, meaning, part_of_speech, source)


def format_response(word_of_the_day, origin, date, usage, meaning, part_of_speech, source):
    """
    Selective key values pairs
    which are retrieved are put
    in an empty dictionary and
    output is shown.
    """

    Dict={}

    Dict["wordOfTheDay"] = word_of_the_day
    Dict["origin"] = origin
    Dict["date"] = date
    Dict["usage"] = usage
    Dict["meaning"] = meaning
    Dict["part_of_speech"] = part_of_speech
    Dict["source"] = source
    email_notification(Dict)


def email_notification(message):
    """
    Instead of seeing every
    new word on the terminal,
    daily the end user gets a 
    email notification regarding
    word of the day.
    """

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_account = os.environ.get('MAIL_ACCOUNT')
    smtp_password = os.environ.get('MAIL_PASSWORD')
    mailto = os.environ.get('MAILTO')
    msg = json.dumps(message, indent=4)
    smtp_server.ehlo()
    smtp_server.starttls()
    try:
        smtp_server.login(smtp_account, smtp_password)
    except smtplib.SMTPAuthenticationError:
        logging.error('Could not login to the smtp server please check your username and password')
        sys.exit(1)
    msg = MIMEText(msg)
    msg['Subject'] = 'Word Of The Day!'
    msg['From'] = smtp_account
    msg['To'] = mailto
    smtp_server.send_message(msg)
    logging.info("Email notification sent!")
    smtp_server.quit()


api_key = os.environ.get('API_KEY')
date = datetime.datetime.today().strftime('%Y-%m-%d')
url = 'http://api.wordnik.com:80/v4/words.json/wordOfTheDay?'+ 'date='+date+'&'+'api_key='+api_key

fetch_response(url)

