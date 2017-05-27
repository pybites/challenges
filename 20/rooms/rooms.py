import platform
import os
import sys
from boxes import Player

"""
Rooms main loop that runs any level
"""

__author__ = "Dante"
__version__ = "0.4"


def clear_screen():
    """ Clears the screen using the correct method for the user's OS """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def print_current_room(r):
    """ Prints the player's current room description, followed by the contents of said Room, with proper spacing """
    print(r.description)
    print()
    print('-=-')
    print()

    if len(r.content) > 1:
        print('Here I can see...')
        for a in r.content:
            print(a.name)
    elif len(r.content) == 1:
        print(f'Here I see {r.content[0].name.lower()}.\n')
    else:
        print()


def print_targets(targets):
    """ Prints the player's current possible action targets, including Actors, movement to other Rooms,
     and inventory checking """
    print('Actions:')
    for k in targets[0]:
        print(f'{k}) {targets[0][k]}')
    print()
    print('Exits:')
    for k in targets[1]:
        print(f'{k}) {targets[1][k]}')
    print()


def ask_for_command():
    """ Asks the user to pick an action or exit """
    return input('Choose your action / exit: ')


def main():
    """ Main entry point of the app, runs level provided as argument in a loop until the player wins """
    try:
        level = __import__(sys.argv[1].replace('.py', '')).Level()
    except IndexError:
        print('No argument provided, using sample level')
        input('Press enter to continue...')
        level = __import__('dantes_adventure').Level()
    except ModuleNotFoundError:
        print('Level not found, using sample level')
        input('Press enter to continue...')
        level = __import__('dantes_adventure').Level()

    player = Player(level.start)
    clear_screen()
    while not player.win:
        r = player.location
        targets = player.possible_action_targets

        print_current_room(r)
        print_targets(targets)

        command = ask_for_command()

        while command not in targets[0] and command not in targets[1]:
            print()
            print('Invalid action, try again.')
            input('Press enter to continue...')
            clear_screen()
            print_current_room(r)
            print_targets(targets)
            command = ask_for_command()
        player.perform_action(command, level)
        print()
        input('Press enter to continue...')
        clear_screen()
    print('You win!')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
