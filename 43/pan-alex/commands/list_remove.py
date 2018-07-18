"""
**** NOT READY FOR INCORPORATION ****
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_delete()
will be executed.
"""

import logging
import re
import os
from commands.list_globals import list_remove_punctuation

DELIMITERS = r'[,;]+|and | from '


def command_remove_correct_syntax(text_no_punc=''):
    """
    This is a function to be wrapped in command_add() and fed a string from
    command_add_remove_punctuation(). This function exists to check that the
    correct syntax was supplied to command_add().

    :param text_no_punc: A string with no punctuation except for those in
    DELIMITERS. Function will look for certain keywords
    based on the syntax:

    "[__], [__], [__] and [__] from ... (___) list ..."

    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * (__) is the name of the list
    * List items must be separated by designated delimiters: 'and' ',' ';'
    * 'from' signals the end of the list items. Anything before 'to' will be added
      to the list, while everything after will be ignored. Only one 'to' should
      be supplied in the sentence.
    * ... are any words that can exist in between key words but are ignored.

    :return: A bool. False if any syntax errors exist and True if no syntax
    errors exist. Conditions checked:

    * 1: 'from' is in the message
    * 2: 'list' is in the message
    * 3: 'from' is not the first word (i.e., the command has a list item to remove)
    * 4: 'from' must come at least one word before 'list' (i.e., the list must
      have a name)
    * 5: No delimiters should appear after the word 'from'
    """
    logging.debug('text_no_punc in command_remove_correct_syntax: ' + text_no_punc)
    text_as_list = text_no_punc.split()

    cond1 = 'from' in text_as_list
    cond2 = 'list' in text_as_list
    logging.debug('cond1: {}; cond2: {}'.format(cond1, cond2))

    if cond1 and cond2:
        cond3 = text_as_list.index('from') > 0
        cond4 = text_as_list.index('from') + 1 < text_as_list.index('list')
        # cond5 is super convoluted. Must improve.
        cond5 = re.split(DELIMITERS, ' '.join(text_as_list[text_as_list.index('from'):]))
        cond5 = len(cond5) == 1
        logging.debug(
            'cond3: {}; cond4: {}; cond5: {}'.format(cond3, cond4, cond5))
        return cond3 and cond4 and cond5
    else:
        return False


def command_remove_edit_file(path, list_items):
    """
    Function intended to be wrapped around command_remove() to provide some
    abstraction in that monstrosity. This function opens the file provided in
    path and saves two lists: one for the items in list_items that are also in
    the file, and one for the items that are not in the file.

    :param path: path to the file containing the list

    :param list_items: list of strings containing list_items that are to be
      removed

    :return: two lists:
    * passed: all items in list_items that are also in the file
    * failed: all items in list_items that are not in the file
    * If 'all' or 'everything' are passed as the only list items, `passed` and
      `failed` will both be empty lists.
    """
    passed = []
    failed = []
    # If the only list item is 'all' or 'everything', delete the contents of the
    # list. command_remove_correct_syntax() will ensure that no empty lists are
    # passed to this function.
    if list_items == ['all'] or ['everything']:
        open(path, 'w').close()
    else:
        with open(path, 'r') as file:
            file_list = file.read().split('\n')
            for item in list_items:
                if item in file_list: passed.append(item)
                else: failed.append(item)
        updated_list = [item for item in file_list if item not in passed]
        # Write the changes
        with open(path, 'w') as file:
                for item in updated_list: file.write(item + '\n')

        logging.debug('passed in command_remove(): ' + str(passed))
        logging.debug('failed in command_remove(): ' + str(failed))

    return passed, failed



def command_remove(sender, other_text=''):
    """
    :param sender: Person who sent the message. This is force-fed to the
      function when called by handle_command(). Does nothing with it.

    :param other_text: String containing any other text in the message that
      was issued after the 'add' command. Function will look for certain keywords
      based on the syntax:

    "remove [__], [__], [__] and [__] from ... (___) list ..."

    * 'remove' is required to call command_remove()
      through handle_command(), but is not actually required inside of
      command_remove.
    * [__] represent list items (things to be removed from the list;
      e.g., 'eggs'). If 'All' is supplied as the only list item, then all of the
      items are removed.
    * ',', 'and', ';' are all delimiters that will separate list items
    * 'from' signals the end of the list items. Anything before 'from' will be
      removed from the list, while everything after will be ignored.
    * ... are any words that can exist in between key words but are ignored.
    * '(__) list' (__) is the name of the list and signals to the bot to look up
      that file in the directory.

    :returns: Opens the file and removes the items from the list. Returns:

    * a message that includes the name of the items removed from the list.
    * If file is empty after deletions, mention that.
    * If no file exists under that name, provide an error message
    * If any items are not in the file, list them.
    """
    logging.debug('command_remove() evaluated.')
    text_no_punc = list_remove_punctuation(other_text)
    logging.debug('text_no_punc in command_remove(): ' + text_no_punc)

    # Check for syntax errors. If none, parse the string to get the list items
    # and the list name
    if not command_remove_correct_syntax(text_no_punc):
        return ("(⊙_☉)7 Sorry... I didn't understand that syntax."
                " Try this: 'remove ___, ___, and ___ from my ___ list.'")
    else:
        # Parse the text by splitting the string at delimiters.
        parsed = [s.strip() for s in re.split(DELIMITERS, text_no_punc) if
                  s.strip()]
        logging.debug('parsed in command_remove(): ' + str(parsed))
        list_items = parsed[:-1]
        # Find the word 'list' and join it to the word directly in front.
        i = parsed[-1].split().index('list')
        list_name = ' '.join(parsed[-1].split()[i - 1:i + 1])

    # Check if a file under the name '____ list.txt' exists.
    path = os.path.join('./lists/', list_name) + '.txt'
    logging.debug('path in command_remove(): ' + str(path))
    if not os.path.isfile(path):
        return "¯\_(ツ)_/¯ Sorry, *{}* doesn't exist.".format(list_name)
    elif os.path.isfile(path):
        passed, failed = command_remove_edit_file(path, list_items)

    # Return message based on conditions below.
    if passed != []:
        removed = ', '.join(passed)
        # All items were in list
        if failed == []:
            response = ("I've removed *{}* from the *{}*!"
                .format(removed, list_name))
        # Some items were in the list
        else:
            not_present = ', '.join(failed)
            response = ("I've removed *{}* from your *{}*, but the following "
                        "were never in the list to start with: *{}*"
                .format(removed, list_name, not_present))
    # None of the items were in the list
    elif failed != []:
        not_present = ', '.join(failed)
        response = ("None of the items you mentioned were on your *{}*. "
                    "You asked to remove: *{}*"
                .format(list_name, not_present))
    # Both lists are empty ('all' or 'everything' was the only list item).
    # See command_remove_edit_file())
    else:
        response = "I've removed all of the items on your {}".format(list_name)

    return response


####

keys = ('remove',)
elements = [command_remove] * len(keys)
COMMANDS_REMOVE = dict(zip(keys, elements))

#### tests to run in Slack
# """
# @bbbot2 remove pizza and cheerios from my grocery list
# @bbbot2 remove eggs, milk, and cheese from my grocery list.
# @bbbot2 remove pizza, a big fat platter, cheerios; and ,,; juice from a new list
# @bbbot2 remove pizza from that one thing... Oh yeah! The grocery list. Thanks!
# @bbbot2 remove make lists from my from-do list    # This should work
# @bbbot2 remove everything from my grocery list.
# @bbbot2 remove all from my grocery list
#
# These should call a failure response
# @bbbot2 remove
# @bbbot2 remove from
# @bbbot2 remove list
# @bbbot2 remove from list
# @bbbot2 remove exercise from my, from-do list
# @bbbot2 remove cheerios, list pizza and cheerios from my grocery list
# @bbbot2 remove everything
# @bbbot2 remove all from list
# """
