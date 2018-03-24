"""
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_delete() will
be executed.
"""
import logging
import os
from commands.list_globals import list_remove_punctuation, list_basic_syntax


def command_delete(sender, other_text=''):
    """
    :param sender: Person who sent the message. This is force-fed to the
      function when called by handle_command(). Does nothing with it.

    :param other_text: String containing any other text in the message that
      was issued after the 'delete' command. Function will look for certain keywords
      based on the syntax:

    "delete ... (___) list ..."

    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * List items must be separated by designated delimiters: 'and' ',' ';'
    * ... are any words that can exist in between key words but are ignored.
    * '(__) list' (__) is the name of the list and signals to the bot to look up
      that file in the directory.

    :returns: Deletes the file if the file exists and is empty. If the file does
      not exist or is not empty, a failure message is returned.
    """
    logging.debug('command_delete() evaluated.')
    text_no_punc = list_remove_punctuation(other_text)

    if not list_basic_syntax(text_no_punc):
        return ("(⊙_☉)7 Sorry... I didn't understand that syntax."
                " Try this: 'delete my grocery list.'")
    else:
        i = text_no_punc.split().index('list')
        list_name = ' '.join(text_no_punc.split()[i - 1:i + 1])
        # Check if a file under the name '____ list.txt' exists.
        path = os.path.join('./lists/', list_name) + '.txt'
        file_exists = os.path.isfile(path)

        if file_exists:
            with open(path, mode='r') as file:
                contents = file.read()
            if contents != '':
                response = ("Your *{a}* is not empty. For safety reasons, "
                            "Make sure you *remove all items from the {a}* "
                            "before deleting it".format(a=list_name))
            else:
                os.remove(path)
                response = ("(҂◡_◡)  I've deleted your {}.".format(list_name))
        else:
            response = ("You don't have a list named *{}*.".format(list_name))

    return response


####

keys = ('delete',)
elements = [command_delete] * len(keys)
COMMANDS_DELETE = dict(zip(keys, elements))

#### tests to run in Slack
# """
# @bbbot2 add pizza and pineapples to my grocery list
# @bbbot2 delete my grocery list
# @bbbot2 delete everything from my grocery list
# @bbbot2 delete my non-existent list!
# @bbbot2 delete
# @bbbot2 delete list
# """
