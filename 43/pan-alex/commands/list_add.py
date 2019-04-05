"""
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_add() will
be executed.
"""
import logging
import re
import os
from commands.list_globals import list_remove_punctuation

DELIMITERS = r'[,;]+|and | to '


# TEST = 'apples, peanuts, oranges and pizza, and apricots to my todo list please'
# TEST = 'pizza, pp, and pineapple to that one thing... Oh yeah! The grocery list. Thanks!'


def command_add_correct_syntax(text_no_punc=''):
    """
    This is a function to be wrapped in command_add() and fed a string from
    list_remove_punctuation(). This function exists to check that the
    correct syntax was supplied to command_add().

    :param text_no_punc: A string with no punctuation except for those in
      DELIMITERS. Function will look for certain keywords
      based on the syntax:

    "[__], [__], [__] and [__] to ... (___) list ..."

    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * List items must be separated by designated delimiters: 'and' ',' ';'
    * 'to' signals the end of the list items. Anything before 'to' will be added
      to the list, while everything after will be ignored. Only one 'to' should
      be supplied in the sentence.
    * ... are any words that can exist in between key words but are ignored.

    :return: A bool. False if any syntax errors exist and True if no syntax
      errors exist. Conditions checked:

    * 1: 'to' is in the message
    * 2: 'list' is in the message
    * 3: 'to' is not the first word (i.e., the command has a list item to add)
    * 4: 'to' must come at least one word before 'list' (i.e., the list must
      have a name)
    * 5: No delimiters should appear after the word 'to'

    """
    logging.debug('text_no_punc in command_add_correct_syntax: ' + text_no_punc)
    text_as_list = text_no_punc.split()

    cond1 = 'to' in text_as_list
    cond2 = 'list' in text_as_list
    logging.debug('cond1: {}; cond2: {}'.format(cond1, cond2))

    if cond1 and cond2:
        cond3 = text_as_list.index('to') > 0
        # 'to' should come before 'list', and there should be at least one word
        # between 'to' and 'list'.
        cond4 = text_as_list.index('to') + 1 < text_as_list.index('list')
        # cond5 is super convoluted. Must improve.
        cond5 = re.split(DELIMITERS, ' '.join(text_as_list[text_as_list.index('to'):]))
        cond5 = len(cond5) == 1
        logging.debug(
            'cond3: {}; cond4: {}; cond5: {}'.format(cond3, cond4, cond5))
        return cond3 and cond4 and cond5
    else:
        return False


def command_add(sender, other_text=''):
    """
    **Note to future self: Implement a way to not write in duplicates**

    :param sender: Person who sent the message. This is force-fed to the
      function when called by handle_command(). Does nothing with it.

    :param other_text: String containing any other text in the message that
      was issued after the 'add' command. Function will look for certain keywords
      based on the syntax:

    "add [__], [__], [__] and [__] to ... (___) list ..."

    * 'add' is required to call command_add() through handle_command(), but is
      not actually required inside of command_add.
    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * ',', 'and', ';' are all delimiters that will separate list items
    * 'to' signals the end of the list items. Anything before 'to' will be added
      to the list, while everything after will be ignored.
    * ... are any words that can exist in between key words but are ignored.
    * '(__) list' (__) is the name of the list and signals to the bot to look up
      that file in the directory.

    :returns: Writes the list items to the specified file as a new line. Returns
      a message that includes all of the items in the list.
      If no file exists under that name, create one and provide a message that a
      new file was created.
    """
    logging.debug('command_add() evaluated.')
    text_no_punc = list_remove_punctuation(other_text)
    logging.debug('text_no_punc in command_add(): ' + text_no_punc)

    if not command_add_correct_syntax(text_no_punc):
        return ("(⊙_☉)7 Sorry... I didn't understand that syntax."
                " Try this: 'add eggs, milk, and cheese to my grocery list.'")
    else:
        # Parse the text by splitting the string at delimiters.
        parsed = [s.strip() for s in re.split(DELIMITERS, text_no_punc) if
                  s.strip()]
        logging.debug('parsed in command_add(): ' + str(parsed))
        list_items = parsed[:-1]
        # Find the word 'list' and join it to the word directly in front.
        i = parsed[-1].split().index('list')
        list_name = ' '.join(parsed[-1].split()[i - 1:i + 1])

    # Check if a file under the name '____ list.txt' exists.
    path = os.path.join('./lists/', list_name) + '.txt'
    file_existed = os.path.isfile(path)

    # Write list items to file
    with open(path, mode='a') as file:
        for item in list_items: file.write(item + '\n')

    # Return response based on whether list existed before or not.
    if file_existed:
        response = "I've added these items to your *{}*: *{}*!".format(
            list_name, str(list_items)[1:-1])
    else:
        response = ("You don't have a list named *{}*. "
                    "Don't worry - I've made one and added these items: *{}* \n"
                    "If this was a mistake, use *remove* and then "
                    "*delete*.".format(list_name, str(list_items)[1:-1]))
    return response


####

keys = ('add',)
elements = [command_add] * len(keys)
COMMANDS_ADD = dict(zip(keys, elements))

#### tests to run in Slack
# """
# @bbbot2 add pizza and cheerios to my grocery list
# @bbbot2 add eggs, milk, and cheese to my grocery list.
# @bbbot2 add pizza, a big fat platter, cheerios; and ,,; juice to a new list
# @bbbot2 add pizza to that one thing... Oh yeah! The grocery list. Thanks!
# @bbbot2 add exercise to my to-do list    # This should work
#
# These should call a failure response
# @bbbot2 add
# @bbbot2 add to
# @bbbot2 add list
# @bbbot2 add to list
# @bbbot2 add exercise to my, to-do list
# @bbbot2 add cheerios, list pizza and cheerios to my grocery list
# """
