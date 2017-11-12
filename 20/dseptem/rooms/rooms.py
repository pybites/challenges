import platform
import os
import sys
from boxes import Player

"""
Rooms main loop that runs any level
"""

__author__ = "Dante"
__version__ = "0.5"


def clear_screen():
    """ Clears the screen using the correct method for the user's OS """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def print_current_room(r):
    """ Prints the player's current room description, followed by the contents of said Room, with proper spacing """
    print(f'{r.description}\n\n-=-\n')

    if len(r.content) > 1:
        print('Here I can see...')
        for a in r.content:
            print(a.name)
    elif len(r.content) == 1:
        print(f'Here I see {r.content[0].name.lower()}.\n')


def print_targets(actions, moves):
    """ Prints the player's current possible action targets, including Actors, movement to other Rooms,
     and inventory checking """
    print('Actions:')
    for k in actions:
        print(k)
    print('\nExits:')
    for k in moves:
        print(k)
    else:
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

    while not player.win:
        r = player.location
        options = {k[0]: k for k in player.actions_and_moves.keys()}

        clear_screen()
        print_current_room(r)
        print_targets(player.actions, player.moves)

        command = ask_for_command()
        if command not in options:
            print('\nInvalid action, try again.')
            input('Press enter to continue...')
            continue

        player_func, param = player.actions_and_moves[options[command]]
        print(f'\n{player_func()}\n') if not param else print(f'\n{player_func(param)}\n')
        input('Press enter to continue...')
    print('You win!')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
