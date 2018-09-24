"""
This command is import into BBbot.py as a commannd that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_hi() will
be executed.
"""
import logging


def command_hi(sender, other_text=None):
    """
    :param sender: Person who sent the message
    :param other_text: Any other text in the message that was issued with the command.
    This is force-fed to the function when called by handle_command(). This
    function does nothing with args.
    :returns: 'Hi <@sender>!'
    """
    logging.debug('command_hi() evaluated.')
    return 'Hi <@{}>!'.format(sender)


keys = ('hi', 'hello', 'hey', 'heya', 'howdy', 'greetings',)
elements = [command_hi] * len(keys)
COMMANDS_HELLO = dict(zip(keys, elements))



#### tests to run in Slack
# @bbbot2 hi how are you?
# @bbbot2 hello!
# @bbbot2 heya
# @bbbot2 greetings robot
# @bbbot2 howdy-yall.
# sup @everyone. @bbbot2 hey what's up

