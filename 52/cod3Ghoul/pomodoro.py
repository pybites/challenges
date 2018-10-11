""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52
    
    The Challenge: 
    - Create a timer for a set duration (eg 20 minutes) that "alarms" or notifies you at completion.
    - Go a step further and allow the user to specify the amount of time the Pomodoro Timer goes for.
    - Further develop the app by allowing it to loop. That is, Pomodoro Time > break time > Pomodoro Time > break time.
    - Create a user interface if you have the time! PyGame or argparse perhaps? Maybe even make it web based with Flask or your other favourite web framework."""


import os
import time


# Global pomodoro counter
pomodoros = 0


def pomodoro_timer(pomodoro_length=25):
    """Time each pomodoro.

    Keyword argument:
    pomodoro_length -- length in minutes of pomodoro (default 25)
    """
    seconds = 0
    minutes = 0
    global pomodoros
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == pomodoro_length:
            pomodoros = pomodoros + 1
            os.system('clear')
            display_pomodoros_completed()
            break
        os.system('clear')
        seconds = seconds + 1
        display_pomodoros_completed()
        display_timer(minutes, seconds)
        time.sleep(1)


def break_between_pomodoros(break_length=5):
    """Time each break between pomodoros.

    Keyword argument:
    break_length -- length in minutes of break (default 5)
    """
    seconds = 0
    minutes = 0
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == break_length:
            os.system('clear')
            display_break(break_length, 'yes')
            break
        os.system('clear')
        seconds = seconds + 1
        display_break(break_length)
        display_timer(minutes, seconds)
        time.sleep(1)


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
    """Display length of break or that the break is over.

    Keyword arguments:
    break_length -- length of break in minutes
    break_over -- signals whether the break has ended
                  using a 'yes' or 'no' string (default = 'no')"""
    if break_over == 'yes':
        print(f'{break_length} minute break is over!')
    else:
        print(f'{break_length} Minute Break: ')


def main():
    """Entry point for program."""
    start = input('Enter S to start your first pomodoro or E to exit: ')
    if start.lower() == 's':
        while True:
            global pomodoros
            pomodoro_timer(3)
            if pomodoros < 4:
                short_break = input('Enter B to start a SHORT break: ')
                if short_break.lower() == 'b':
                    break_between_pomodoros(1)
            if pomodoros == 4:
                long_break = input('Enter B to start a LONG break: ')
                if long_break.lower() == 'b':
                    break_between_pomodoros(2)
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
                return
    else:
        return


if __name__ == '__main__':
    main()

