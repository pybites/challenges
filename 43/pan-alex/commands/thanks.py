"""
This command is import into BBbot.py as a commannd that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_thanks()
will be executed. This works basically the same way as command_hi().
"""
import logging


def command_thanks(sender, other_text=None):
    """
    :param sender: Person who sent the message
    :param other_text: Any other text in the message that was issued with the command.
    This is force-fed to the function when called by handle_command(). This
    function does nothing with args.
    :returns: 'Hi <@sender>!'
    """
    logging.debug('command_thanks() evaluated.')
    return " (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧  You're welcome <@{}>!  ✧ﾟ･: *ヽ(◕ヮ◕ヽ)".format(sender)


keys = ('thank', 'thanks')
elements = [command_thanks] * len(keys)
COMMANDS_THANKS = dict(zip(keys, elements))



#### tests to run in Slack
# @bbbot2 thank you!
# @bbbot2 thanks@@