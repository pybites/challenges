import platform
import os
from boxes import Player
import dantes_adventure

"""
Rooms main loop that runs any level
"""

__author__ = "Dante"
__version__ = "0.3.0"


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def print_current_room(r):
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
    print('Actions:')
    for k in targets[0]:
        print(f'{k}) {targets[0][k]}')
    print()
    print('Exits:')
    for k in targets[1]:
        print(f'{k}) {targets[1][k]}')
    print()


def ask_for_command():
    return input('Choose your action / exit: ')


def main():
    """ Main entry point of the app """
    map = dantes_adventure.DanteLevel()
    player = Player(map.start)
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
        player.perform_action(command, map)
        print()
        input('Press enter to continue...')
        clear_screen()
    print('You win!')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
