""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52
    
    The Challenge: 
    - Create a timer for a set duration (eg 20 minutes) that "alarms" or notifies you at completion.
    - Go a step further and allow the user to specify the amount of time the Pomodoro Timer goes for.
    - Further develop the app by allowing it to loop. That is, Pomodoro Time > break time > Pomodoro Time > break time.
    - Create a user interface if you have the time! PyGame or argparse perhaps? Maybe even make it web based with Flask or your other favourite web framework."""


from os import system
from time import sleep


# Default Pomodoro Settings:
# [number of pomodoros,
#  length in minutes of each pomodoro,
#  length in minutes of each short break,
#  length in minutes of each long break]
DEFAULT_SETTINGS = [4, 25, 5, 20]
pomodoros = 0


def pomodoro_timer(pomodoro_length):
    """Timer for each pomodoro.

    Keyword argument:
    pomodoro_length -- length in minutes of pomodoro
    """
    global pomodoros
    seconds = 0
    minutes = 0
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == pomodoro_length:
            pomodoros += 1
            system('clear')
            display_pomodoros_completed()
            break
        system('clear')
        seconds = seconds + 1
        display_pomodoros_completed()
        display_timer(minutes, seconds)
        sleep(1)


def break_timer(break_length):
    """Timer for each break.

    Keyword argument:
    break_length -- length in minutes of break
    """
    seconds = 0
    minutes = 0
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == break_length:
            system('clear')
            display_break(break_length, 'yes')
            break
        system('clear')
        seconds = seconds + 1
        display_break(break_length)
        display_timer(minutes, seconds)
        sleep(1)


def display_timer(minutes, seconds):
    """Display the active timer on screen.

    Keyword arguments:
    minutes -- minutes to display on screen when this method is called
    seconds -- seconds to display on screen when this method is called
    """
    print(f'{minutes} {"Min" if minutes == 1 else "Mins"} {seconds} Secs')


def display_pomodoros_completed():
    """Display the total number of Pomodoros completed."""
    global pomodoros
    print(f'Pomodoros Completed: {pomodoros}\n')


def display_break(break_length, break_over='no'):
    """Display the length of the current break or if the break is over.

    Keyword arguments:
    break_length -- length of break in minutes
    break_over -- signals whether the break has ended
                  using a 'yes' or 'no' string (default 'no')
    """
    if break_over == 'yes':
        print(f'{break_length} minute break is over!')
    else:
        print(f'{break_length} Minute Break: ')


def display_start_menu():
    """Displays the main start menu with options for the user to either
    choose their own times (in minutes) for each pomodoro, short break,
    and long break, or go with the default values listed below.
    The menu also provides the user the option to choose how many pomodoros
    they would like to complete before each long break or also they can go
    with the default listed below.
    
    Default values:
    Number of pomodoros to complete one set: 4
    Length of each pomodoro: 25
    Length of each short break between pomodoros: 5
    Length of each long break after one set of pomodoros is completed: 20
    """
    print('\n\tWelcome to Your Pomodoro Timer!!\n\n')
    print('If you would like to start a set of pomodoros using the default\n'
          'values of 4 pomodoros per set with the length of each pomodoro\n'
          '25 minutes long, a 5 minute break between each pomodoro, and a\n'
          '20 minute break after completing a full set of pomodoros, then\n'
          'enter "default" at the prompt.\n\n'
          'However if you would like to specify your\n'
          'own times and number of pomodoros, '
          'then enter "set" at the prompt.\n\n')


def user_defined_settings():
    """Prompts the user to set the variables they would like to use
    for the program, if they choose not to use the defaults.
    """
    confirmed = False

    while confirmed is not True:
        num_of_pomos = input('\nEnter the number of pomodoros you would like '
                             'to complete per set: ')
        len_of_pomos = input('\nEnter the length in minutes of each '
                             'pomodoro: ')
        len_of_short_break = input('\nEnter the length in minutes for each '
                                    'short break between pomodoros: ')
        len_of_long_break = input('\nEnter the length in minutes for each '
                               'long break after a full set of pomodoros '
                               'is completed: ')

        print(f'\nYou have set your pomodoro timer up with the following '
              f'configuration:\n'
              f'\n\tNumber of Pomodoros per Set: {num_of_pomos}'
              f'\n\tLength of Each Pomodoro: {len_of_pomos}'
              f'\n\tLength of Each Short Break: {len_of_short_break}'
              f'\n\tLength of Each Long Break: {len_of_long_break}')
        
        while True:
            confirm = input('\nTo confirm these settings enter "confirm" or '
                            'to change them enter "change": ')
            if confirm.lower() == 'confirm':
                confirmed = True
                break
            elif confirm.lower() == 'change':
                break
            else:
                print('\nYou did not enter "confirm" or "change" at the '
                      'previous prompt.\n')

    return [int(num_of_pomos), int(len_of_pomos), int(len_of_short_break), int(len_of_long_break)]


def start_pomodoro(settings):
    global pomodoros
    while True:
        pomodoro_timer(settings[1])
        if pomodoros < settings[0]:
            short_break = input('Enter B to start a SHORT break: ')
            if short_break.lower() == 'b':
                break_timer(settings[2])
        if pomodoros == settings[0]:
            long_break = input('Enter B to start a LONG break: ')
            if long_break.lower() == 'b':
                break_timer(settings[3])
        con = input('\n1) Enter S to start your next pomodoro.\n'
                    '2) Enter R to reset your pomodoro count\n'
                    '   and start a new set of pomodoros.\n'
                    '3) Enter E to exit.\n\n'
                    'Choose one of the above options: ')
        if con.lower() == 's':
            continue
        elif con.lower() == 'r':
            pomodoros = 0
            continue
        else:
            break
    return


def main():
    """Entry point for program."""
    display_start_menu()
    while True:
        start = input('Enter "default" or "set" to begin, ' 
                      'or "exit" to exit program: ')
        if start.lower() == 'set':
            custom_settings = user_defined_settings()
            start_pomodoro(custom_settings)
            break
        elif start.lower() == 'default':
            start_pomodoro(DEFAULT_SETTINGS)
            break
        elif start.lower() == 'exit':
            break
        else:
            print('\nYou did not enter "default", "set", or "exit".\n')
            continue
    print('\n\tThank you for using my pomodoro. Hope it worked for you!\n')


if __name__ == '__main__':
    main()

