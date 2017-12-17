# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 08:29:08 2017

@author: clamytoe
"""
import time
import requests
from functools import lru_cache
from random import choice
from bs4 import BeautifulSoup
from slackclient import SlackClient
# from config import BOT_ID, SLACK_BOT_TOKEN
from keys import BOT_ID, SLACK_BOT_TOKEN

# connect to the Slack API
SLACK_CLIENT = SlackClient(SLACK_BOT_TOKEN)

AT_BOT = f'<@{BOT_ID}>'
READ_DELAY = 1


def get_image(topic):
    """
    Returns an image URL based on the search topic.

    :param topic: String - What to search for
    :return: String - URL of a random image
    """
    site = 'wallhaven.cc'
    pattern = topic.lower().replace(' ', '+')
    url = f'https://alpha.{site}/search?q={pattern}&categories=111&purity=100&sorting=random&order=desc'
    wallpaper = soup_magic(url)

    return wallpaper


def soup_magic(url):
    """
    BeautifulSoup scraping code.

    :param url: String - the URL of the page to scrape
    :return: None or bs4.element.Tag - the bs4 image tag object
    """
    # handle a no connection error
    try:
        # search for the topic and pick a random thumbnail
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')
        thumb_tags = soup.find_all('a', {'class': 'preview'})
        images = [html_tag['href'] for html_tag in thumb_tags]
    except requests.exceptions.ConnectionError:
        return None

    # handle a no match situation
    try:
        image_url = choice(images)

        # scrape the actual image
        image_page = requests.get(image_url)
        image_soup = BeautifulSoup(image_page.content, 'html5lib')
        image = image_soup.find('img', {'id': 'wallpaper'})

        return image
    except IndexError:
        return None


def search_for_topic(topic, channel, username):
    """
    Receives the search string directed at the bot and searches for the topic.

    If a match is found it returns a the image, if not, it lets the user know.

    :param topic: String - the topic that was given to the bot
    :param channel: String - the name of the channel from where the command was given
    :param username: String - the username of the person issuing the command
    :return: None
    """
    if topic:
        response = f'<{username}> just a sec while I search for an image based on *{topic}*...'
        post_message(response, channel)
        wallpaper = get_image(topic)

        # return the wallpaper image that was found
        if wallpaper:
            title = wallpaper['alt']
            src = f"<https:{wallpaper['src']}>"
            found_response = f'*{title}*\n{src}'
            post_message(found_response, channel)
        else:
            # if nothing is found, let the user know
            response = f"Sorry <{username}>, I tried but I couldn't find anything like that..."
            post_message(response, channel)


@lru_cache(maxsize=128)
def lookup_user(user_id):
    """
    Looks up the username of the given user id.

    :param user_id: String - Slack ID of the user
    :return: String - Username of the user
    """
    user_info = SLACK_CLIENT.api_call('users.info', user=user_id)
    user_name = f'@{user_info["user"]["name"]}'
    return user_name


def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API parsing function.

    Returns None unless a message is directed at the Bot, based on its ID.

    :param slack_rtm_output: List - contents of RTM Slack Read
    :return: Tuple - (None, None, None) or (topic, channel, username)
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                topic = output['text'].split(AT_BOT)[1].strip().lower()
                channel = output['channel']
                username = lookup_user(output['user'])
                return topic, channel, username
    return None, None, None


def post_message(response, channel):
    """
    Takes the response given and posts it to the channel provided.

    :param response: String - response to be posted to the channel
    :param channel: String - the channel were the response is to be posted to
    :return: None
    """
    SLACK_CLIENT.api_call('chat.postMessage', channel=channel, text=response, as_user=True)


def run_bot():
    """
    Starts the bot.

    :return: None
    """
    if SLACK_CLIENT.rtm_connect():
        print('Bot connected and running!')
        while True:
            (topic, channel, user_name) = parse_slack_output(SLACK_CLIENT.rtm_read())
            if topic and channel:
                search_for_topic(topic, channel, user_name)
            time.sleep(READ_DELAY)
    else:
        print('Connection failed, invalid Slack TOKEN or bot ID?')


if __name__ == '__main__':
    run_bot()
