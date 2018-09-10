'''
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_show() will
be executed.
'''
import logging
import os
from commands.list_globals import list_remove_punctuation


def command_show(sender, other_text=''):
    """
    :param sender: Person who sent the message. This is force-fed to the
      function when called by handle_command(). Does nothing with it.

    :param other_text: String containing any other text in the message that
      was issued after the 'show' command. Compared to other list commands,
      `show` as a very simple syntax:

    "show lists ..."

    * lists is a folder containing all of the lists. While this function was
      originally designed to display a bunch of text files in a folder, it is
      also possible to look at other folders (if you know the correct path)
    * ... is text that comes after lists that will be ignored.

    :returns: The contents of the folder, or a failure message if no folder
      exists.
    """
    logging.debug('command_show() evaluated.')

    text_no_punc = list_remove_punctuation(other_text).split()
    if text_no_punc == []: path = 'lists'    # Default to directory 'lists'
    else: path = text_no_punc[0]

    path_exists = os.path.isdir(path)
    if path_exists:
        files = '\n'.join(os.listdir(path))
        response = "Here are the files stored in *{}*: \n{}".format(
            path, files)
    else:
        response = ("ಠ_ಠ  There is no directory named *{}*.".format(path))

    return response


####

keys = ('show',)
elements = [command_show] * len(keys)
COMMANDS_SHOW = dict(zip(keys, elements))

#### tests to run in Slack
# '''
# @bbbot2 show
# @bbbot2 show lists
# @bbbot2 show commands
# @bbbot2 show nonexistant
# '''