# -*- coding: utf-8 -*-
from keys import BOT_ID, BOT_NAME, CHANNEL_ID, SLACK_BOT_TOKEN
import mohhsbot


def test_environment_variables():
    assert BOT_ID == 'U854JKLNS'
    assert BOT_NAME == 'mohh'
    assert CHANNEL_ID.startswith('xoxp')
    assert SLACK_BOT_TOKEN.startswith('xoxb')


def test_slack_connection():
    assert isinstance(mohhsbot.SLACK_CLIENT, mohhsbot.SlackClient)


def test_bot_id():
    assert mohhsbot.AT_BOT == f'<@{BOT_ID}>'

