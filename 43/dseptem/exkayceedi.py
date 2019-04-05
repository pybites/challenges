import time
import re

import slackclient
import requests

from dni import SLACK_NAME, SLACK_TOKEN, SLACK_ID

# delay in seconds before checking for new events
SOCKET_DELAY = 1

sc = slackclient.SlackClient(SLACK_TOKEN)


# how the bot is mentioned on slack
def get_mention(user):
    return '<@{user}>'.format(user=user)


slack_mention = get_mention(SLACK_ID)


def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    t = event.get('type')
    if t and t == 'message' and not(event.get('user') == SLACK_ID):
        # in case it is a private message return true
        if is_private(event):
            return True
        # in case it is not a private message check mention
        text = event.get('text')
        print(text.strip().split())
        if slack_mention in text.strip().split():
            return True


def wants_latest(message):
    if 'latest' in message.strip().split():
        return True
    return False


def wants_specific(message):
    strip_n = re.search('#(\d+)', message)
    if strip_n:
        return strip_n.group(1)
    return False


def get_xkcd(number):
    if number == 0:
        data = requests.get('https://xkcd.com/info.0.json')
    else:
        data = requests.get(f'https://xkcd.com/{number}/info.0.json')
    if data.status_code != 200:
        return False
    j = data.json()
    return j


def give_xkcd(number, user_mention):
    j = get_xkcd(number)
    if not j:
        return f"Sorry, there was an error retrieving that strip..."
    return f"{user_mention}\nTitle: {j['safe_title']}\nStrip #{j['num']}\nLink: {j['img']}\nAlt Text: {j['alt']}"


def handle_message(message, user, channel):
    user_mention = get_mention(user)
    if wants_latest(message):
        post_message(message=give_xkcd(0, user_mention), channel=channel)

    specific = wants_specific(message)
    if specific:
        post_message(message=give_xkcd(specific, user_mention), channel=channel)


def post_message(message, channel):
    sc.api_call('chat.postMessage', channel=channel,
                text=message, as_user=True)


def is_private(event):
    """Checks if private slack channel"""
    return event.get('channel').startswith('D')


def run():
    if sc.rtm_connect():
        print('[.] Exkayceedi, online!...')
    else:
        print('[!] Connection to Slack failed.')
        return
    while True:
        event_list = sc.rtm_read()
        try:
            for event in event_list:
                if is_for_me(event):
                    handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
        except:
            print('No events or error handling message')
        time.sleep(SOCKET_DELAY)


if __name__ == '__main__':
    run()
