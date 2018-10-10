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
            if pomodoros == 1:
                print('You have completed 1 pomodoro.')
            else:
                print(f'You have completed {pomodoros} pomodoros.')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'Pomodoros Completed: {pomodoros}\n')
            print(f'1 Min {seconds} Secs')
        else:
            print(f'Pomodoros Completed: {pomodoros}\n')
            print(f'{minutes} Mins {seconds} Secs')
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
            print(f'{break_length} minute break is over!')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'{break_length} Minute Break: {minutes} Min {seconds} '
                  f'Secs')
        else:
            print(f'{break_length} Minute Break: {minutes} Mins {seconds} '
                  f'Secs')
        time.sleep(1)


def main():
    """Entry point for program."""
    start = input('Enter S to start your first pomodoro or E to exit: ')
    if start.lower() == 's':
        while True:
            global pomodoros
            pomodoro_timer()
            if pomodoros < 4:
                short_break = input('Enter B to start a SHORT break: ')
                if short_break.lower() == 'b':
                    break_between_pomodoros()
            if pomodoros == 4:
                long_break = input('Enter B to start a LONG break: ')
                if long_break.lower() == 'b':
                    break_between_pomodoros(20)
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

