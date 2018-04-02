"""
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_read() will
be executed.
"""
import logging
import os
from commands.list_globals import list_remove_punctuation, list_basic_syntax


def command_read(sender, other_text=''):
    """
    :param sender: Person who sent the message. This is force-fed to the
      function when called by handle_command(). Does nothing with it.

    :param other_text: String containing any other text in the message that
      was issued after the 'read' command. Function will look for certain
      keywords based on the syntax:

    "read  ... (___) list ..."

    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * List items must be separated by designated delimiters: 'and' ',' ';'
    * ... are any words that can exist in between key words but are ignored.
    * '(__) list' (__) is the name of the list and signals to the bot to look up
      that file in the directory.

    :returns: The contents of the list with each item on a new line, or a
      failure message if no file exists.
    """
    logging.debug('command_read() evaluated.')
    text_no_punc = list_remove_punctuation(other_text)

    if not list_basic_syntax(text_no_punc):
        return ("(⊙_☉)7 Sorry... I didn't understand that syntax."
                " Try this: 'read me my grocery list.'")
    else:
        i = text_no_punc.split().index('list')
        list_name = ' '.join(text_no_punc.split()[i - 1:i + 1])
        # Check if a file under the name '____ list.txt' exists.
        path = os.path.join('./lists/', list_name) + '.txt'
        file_exists = os.path.isfile(path)
    if file_exists:
        with open(path, mode='r') as file:
            list_items = str(file.read())
            logging.debug('items in file.read() in command_read(): ' + list_items)
        response = "Here's what's on your *{}*: \n{}".format(
            list_name, list_items)
    else:
        response = ("You don't have a list named *{}*.".format(list_name))

    return response


####

keys = ('read',)
elements = [command_read] * len(keys)
COMMANDS_READ = dict(zip(keys, elements))

#### tests to run in Slack
# """
# @bbbot2 read my grocery list
# @bbbot2 read eggs, milk, and cheese to my grocery list.
# @bbbot2 read pizza, a big fat platter, cheerios; and ,,; juice a new list
# @bbbot2 read .................... sjoFHSJF AS;ALKDJA; The grocery list. Thanks!
# @bbbot2 read
# @bbbot2 read list
# """
