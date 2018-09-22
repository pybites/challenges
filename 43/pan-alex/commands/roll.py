"""
This command is import into BBbot.py as a command that the Slack bot can
handle. When called by any of the keywords listed in `keys`, command_roll() will
be executed.
"""
import logging
import random


def command_roll(sender, other_text=''):
    """
    :param sender: Person who sent the command
    :param other_text: A string containing all of the words following the
    command itself. The function looks integers inside this list and uses the
    first integer it encounters as the number of sides on the die.
    :return: Randomly generates an integer between 1 and the number of sides on
    the die. If no number is supplied in args, it defaults to 20.
    """
    logging.debug('command_roll() evaluated.')
    logging.debug('other_text in command_roll: ' + other_text)
    sides_on_die = 20

    args = other_text.translate(other_text.maketrans('-', ' ')).split()
    logging.debug('args in command_roll: ' + str(other_text))

    if args:
        for item in args:
            logging.debug('item in command_roll: ' + str(item))
            if item.isnumeric() and int(item) > 1:
                sides_on_die = int(item)
                break
    logging.debug('sides_on_die in command_roll: ' + str(sides_on_die))

    roll = random.randint(1, sides_on_die)

    if roll == 1: emote = '(╯°□°）╯︵ ┻━┻ '
    elif roll == sides_on_die: emote = '(づ◕‿◕)づ '
    else: emote = ''
    logging.debug('emote: ' + str(emote))
    return '{}<@{}> rolled {} on a {}-sided die!'.format(
        emote, sender, roll, sides_on_die)

####

keys = ('roll', 'dice', 'die')
elements = [command_roll] * len(keys)
COMMANDS_ROLL = dict(zip(keys, elements))


#### tests to run in Slack

# # roll 0.5 and -5 return a 5-sided die. This is because punctuation chars
# # are replaced with spaces so the integers are read separately from punctuation
# # marks. I can't decide it this is a bug or a feature.
# @bbbot2 roll
# @bbbot2 roll 0.5    # function does not interpret decimals. return 20
# @bbbot2 roll -5    # Number below 1
# @bbbot2 roll 0    # Number below 1; should roll 20
# hey @bbbot2 roll a 30 sided die for me!
# @bbbot2 roll a 400-sided die
# @bbbot2 roll 50.2    # function does not interpret decimals. return 20
# @bbbot2 roll 2    # Roll until you get 1 and 2
#
# # These are evaluated the same way as roll. I only need to check that these
# # commands properly call the function.
# @bbbot2 die
# @bbbot2 die something 30
# @bbbot2 dice
# @bbbot2 dice 50.2
