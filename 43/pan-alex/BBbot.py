"""The code used to initialize the bot is based on fullstackpython
https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
and Pybites https://github.com/pybites/slackbot

slack_bot() is the main function that execute's the bot's code. slack_bot()
carries out the process below:

1. find_slack_commands searches Slack events for mentions aimed at the bot and
    feeds the text to handle_command()
2. handle_command() wraps around parse_command(), which parses the command from
    the rest of the message and returns it to handle_command().
3. handle_command() searches a dictionary to see if the command exists. If so,
    it executes the command (code for each command can be found in the
    'commands' subfolder). If not, it returns a failure message.

New commands are added by importing the functions from the `commands` subfolder.
Functions are imported as dictionary entries; key = text that call the command,
value = function that executes the call). The commands are made functional by
updateding the COMMANDS dict.
"""

import time
import logging
import string
from slackclient import SlackClient

# Commands
from commands.hello import COMMANDS_HELLO
from commands.thanks import COMMANDS_THANKS
from commands.roll import COMMANDS_ROLL
from commands.list_add import COMMANDS_ADD
from commands.list_remove import COMMANDS_REMOVE
from commands.list_read import COMMANDS_READ
from commands.list_delete import COMMANDS_DELETE
from commands.list_show import COMMANDS_SHOW


# ¯\_(ツ)_/¯

logging.getLogger().setLevel(logging.CRITICAL)

# Constants
# SLACK_BOT_TOKEN is stored in a c file to keep it out of version control.
SLACK_BOT_TOKEN = open('Bot User OAuth Access Token.c').read()
BOT_ID = 'U8HGESKV0'    # Can be retrieved by clicking on the bot in Slack
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# Create an instance of the Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN)


############

def command_help(sender, other_text=''):
    """
    :param sender: The sender, which is force-fed to the function when it is
      called by handle_command(). Does nothing with it.

    :param args: Any text after the word 'help'. Likewise, args are force-fed to
      the function when it is called by handle_command(). Does nothing with them.

    :return: Outputs a list of valid commands.
    """
    response = ("Here is a list of commands that I know how to respond to. "
                "Use the syntax: '{} *command*' so that I know you're talking"
                "to me!").format(AT_BOT)
    # Append the list of commands. Crop out brackets
    response += str(sorted(COMMANDS))[1:-1]
    response += ("\nStill confused? Read how I work at "
        "https://github.com/pan-alex/slack_bot")
    
    return response


#################

# Commands are kept in the commands subfolder. When a new command is added, the
# dictionary here is updated. The key is the text that the user types to call
# the command; the value is the function that will be executed.
COMMANDS = {'help': command_help}
COMMANDS.update(COMMANDS_HELLO)
COMMANDS.update(COMMANDS_THANKS)
COMMANDS.update(COMMANDS_ROLL)
COMMANDS.update(COMMANDS_ADD)
COMMANDS.update(COMMANDS_REMOVE)
COMMANDS.update(COMMANDS_READ)
COMMANDS.update(COMMANDS_DELETE)
COMMANDS.update(COMMANDS_SHOW)

#################


def parse_command(text):
    """
    Intended to wrapped by handle_command().

    :text: A string. The Slack message directed at the bot, minus the <@bot>
      mention itself.

    :return: Converts punctuation on the first word to spaces and interprets the
      first word as the command. Returns the remaining text as a string without
      punctuation stripping.
    """
    s = string.punctuation
    command = text.translate(text.maketrans(s, ' ' * len(s))).split()[0]
    other_text = ' '.join(text.split()[1:])
    return command, other_text


def handle_command(text, channel, sender):
    """
    :param text:  A text string containing a command directed at the bot

    :param channel: A string containing the channel that the command was given
      from.

    :return: If command is a valid command, execute that command. If not,
      display a message that the command is not valid.
    """
    command, other_text = parse_command(text)

    if command in COMMANDS:
        if other_text: response = COMMANDS[command](sender, other_text,)
        else: response = COMMANDS[command](sender,)
    else:
        response = (
            "(´･_･`) Sorry <@{}>... No one ever taught me how to answer that."
            "\n (use *help* for a list of available commands)".format(sender,))

    slack_client.api_call('chat.postMessage', channel=channel,
                          text=response, as_user=True)


def find_slack_commands(events):
    """
    Parses slack events for direct mentions of the bot.

    :param events: An event is anything remotely interesting that happens in
      Slack. Messages, user status changes, and users typing are all events. Each
      event is stored as a dictionary and the events are stored in a list. Certain
      elements of the event can be extracted using dict functionality.

    :return: If an event directly mentions the bot (ignoring self-mentions by
      the bot), return the text (all lowercase), the channel, and the user that
      sent the command. Otherwise return None for all.

    """
    if events and len(events) > 0:
        logging.debug('event in find_slack_commands(): ' + str(events))
        for event in events:
            # Parse events that contain text mentioning the bot.
            if event and 'text' in event and AT_BOT in event['text']:
                # return text after the @ mention, whitespace removed
                text = event['text'].split(AT_BOT)[1].strip().lower()
                channel = event['channel']
                # Don't evaluate if bot calls its own name
                if event['user'] == BOT_ID: break

                # Retrieve sender's display name
                user = slack_client.api_call('users.info', user=event['user'])
                sender = user['user']['name']
                logging.debug('text, channel, user find_slack_commands(): '
                              '{}, {}, {}'.format(text, channel, sender))
                return text, channel, sender
    return None, None, None


def slack_bot(read_delay=1):
    """
    Initializes the bot. Once initialized, the bot will run through an infinite
    loop where it will check all slack events for messages that are directed at
    it (via find_slack_commands). Any direct messages are passed to
    handle_command, which will attempt to execute the command.

    :param read_delay: Implements a 1 second delay between each loop of of the
      function to prevent CPU overload.

    :return: If the bot successfully connects, it will display a success
      message. If it fails, display a failure message. Outputs from handle_command
      are posted directly to Slack.
    """
    if slack_client.rtm_connect():
        print("BBbot is connected and running!")
        # Command below can be used to retrieve ID
        logging.debug('Bot ID: ' + slack_client.api_call('auth.test')['user_id'])
        while True:
            command, channel, user = find_slack_commands(slack_client.rtm_read())
            if command and channel and user:
                handle_command(command, channel, user)
            time.sleep(read_delay)
    else:
        print("Connection failed. Check Slack token and/or bot ID")


if __name__ == "__main__":
    slack_bot()