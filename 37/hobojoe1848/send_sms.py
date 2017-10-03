import os
import sqlite3

from twilio.rest import Client
from sms_recipients import PH_NUMBERS

DATA_FILE = 'steam_games.db'
recipients = PH_NUMBERS
account_sid =      #os.env variable for Twilio Account SID here
auth_token =       #os.env variable for Twilio Auth Token here

client = Client(account_sid, auth_token)

def pull_data():
    text = ''
    with sqlite3.connect(DATA_FILE) as connection:
        c = connection.cursor()
        c.execute("SELECT Name, Link FROM new_steam_games WHERE Emailed='0'")
        for item in c.fetchall():
            text += item[0] + ': ' + item[1] + '\n\n'
        c.execute("UPDATE new_steam_games SET Emailed='1'")
    return text

def send_sms(text, recipients):
    for user in recipients:
        message = client.messages.create(
            to=user,
            from_="<TWILIO NUMBER HERE>",
            body=text
        )
    return message.sid
    
if __name__ == '__main__':
    send_sms(pull_data(), recipients)
