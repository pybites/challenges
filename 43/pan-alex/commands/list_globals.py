""" Some functions and globals are shared between all of the list commands so
that they share the same syntax. These are in this file and then imported to
each list command to avoid any circular dependencies.
"""

# same as string.punctuation but exclude: , ; - (keep hyphenated words)
PUNCTUATION = '!"#$%&\'()*+./:<=>?@[\\]^_`{|}~'

def list_remove_punctuation(other_text=''):
    """
    This is a function to be wrapped in the list commands (i.e., files
    with the names 'list_xyz.py'

    :param other_text: String containing any other text in the message that
    was issued after the 'add' command. Will remove any punctuation, other than
    those in DELIMITERS.

    :return: Returns a string, which is other_text with the punctuation removed.
    """
    text_no_punc = other_text.translate(
        other_text.maketrans(PUNCTUATION, ' ' * len(PUNCTUATION)))
    return text_no_punc


def list_basic_syntax(text_no_punc=''):
    """
    This is a function to be wrapped in command_read() and command_delete(). It
    is fed a string from list_remove_punctuation(). This function exists to
    check that the correct syntax was supplied to command_read() or
    command_delete(). The other list functions have more complex syntax, so
    they have their own 'correct syntax' function.

    :param text_no_punc: A string with no punctuation except for those in
      DELIMITERS. Function will look for certain keywords
      based on the syntax:

    " ... (___) list ..."

    * [__] represent list items (things to be added to the list; e.g., 'eggs')
    * List items must be separated by designated delimiters: 'and' ',' ';'
    * ... are any words that can exist in between key words but are ignored.
    * '(__) list' (__) is the name of the list and signals to the bot to look up
      that file in the directory.

    :return: A bool. False if any syntax errors exist and True if no syntax
    errors exist. Conditions checked:
    """
    text_as_list = text_no_punc.split()

    cond1 = 'list' in text_as_list
    cond2 = len(text_as_list) > 1
    return cond1 and cond2
