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
            minutes += 1
        if minutes == pomodoro_length:
            pomodoros += 1
            system('clear')
            display_pomodoros_completed()
            break
        system('clear')
        seconds += 1
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
            minutes += 1
        if minutes == break_length:
            system('clear')
            display_break(break_length, 'yes')
            break
        system('clear')
        seconds += 1
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
    print('If you would like to start a Pomodoro Timer using the default '
          'settings below, then enter "default" at the prompt.\n\n'
          '\tDefault values:\n'
          '\tNumber of pomodoros to complete one set: 4\n'
          '\tLength of each pomodoro: 25 minutes\n'
          '\tLength of short breaks between pomodoros: 5 minutes\n'
          '\tLength of long break after one set of pomodoros: 20 minutes\n\n'
          'However, if you would like to customize the settings for your '
          'Pomodoro Timer, then enter "custom" at the prompt.\n\n')


def user_defined_settings():
    """Prompts the user to set the variables they would like to use
    for the program, if they choose not to use the defaults.
    """
    print('\n\n\t** After entering your settings and confirming them, '
          'your first pomodoro timer will start **\n')

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
              f'settings:\n'
              f'\n\tNumber of Pomodoros per Set: {num_of_pomos}'
              f'\n\tLength of Each Pomodoro: {len_of_pomos}'
              f'\n\tLength of Each Short Break: {len_of_short_break}'
              f'\n\tLength of Each Long Break: {len_of_long_break}')

        print('\n*Remember, as soon as you enter "confirm" at the prompt '
              'below, your first pomodoro will start using your chosen '
              'settings.')
        
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
            short_break = input('Enter "b" to start your short break: ')
            if short_break.lower() == 'b':
                break_timer(settings[2])
                print('\n> Enter "s" to start your next pomodoro.')
        if pomodoros == settings[0]:
            long_break = input('Enter "b" to start your long break: ')
            if long_break.lower() == 'b':
                break_timer(settings[3])
                print(f'\n** You have completed a set of {settings[0]} '
                      f'{"pomodoro" if settings[0] == 1 else "pomodoros"}.\n')
        print('> Enter "r" to reset your pomodoro count '
              'and start a new set of pomodoros using your '
              'existing settings.\n'
              '> Enter "m" to exit to the main menu.\n\n')
        while True:
            con = input('Choose one of the above options: ')
            if con.lower() == 's':
                break
            elif con.lower() == 'r':
                pomodoros = 0
                break
            elif con.lower() == 'm':
                return
            else:
                print('\n*You did not enter one of the above options.\n')
                continue


def main():
    """Entry point for program."""
    while True:
        system('clear')
        display_start_menu()
        start = input('Enter "default" or "custom" to begin, ' 
                      'or "quit" to quit the program: ')
        if start.lower() == 'custom':
            custom_settings = user_defined_settings()
            start_pomodoro(custom_settings)
            continue
        elif start.lower() == 'default':
            start_pomodoro(DEFAULT_SETTINGS)
            continue
        elif start.lower() == 'quit':
            print('\n\tThank you for using my Pomodoro Timer! '
                  'I hope you enjoyed using it!!\n')
            break
        else:
            print('\n*You did not enter "default", "custom", or "quit".\n')
            continue


if __name__ == '__main__':
    main()
