from datetime import timedelta
from datetime import datetime
import os
import time


def welcome():
    """Like a banner"""
    print('Hello from Pomodoro Timer =)')
    time.sleep(1)
    print("Let's go")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print('Go!')


def main(task):
    """Aggregated func"""
    while True:
        if task == 'start':
            pomodoro_limit = input(
                '\nPlease enter time limit for Pomodoro timer (default is 25 minutes):')
            long_break_limit = input(
                "\nPlease select one of the options of long break timer (15/30 minutes): ")
            pomodoro_flow(pomodoro_limit, long_break_limit)
        elif task == 'stop':
            print('Buy :)')
            break
        else:
            print('Value is incorrect')
            task = input('Please Enter one of the actions (start/stop): ')


def pomodoro_flow(pomodoro_time, long_relax_time):
    """For both timers rest and work"""
    standard_seq = 4
    short_relax_time = 5
    while standard_seq > 1:
        standard_seq -= 1
        pomodoro_timer(pomodoro_time)
        break_timer(short_relax_time)
    else:
        pomodoro_timer(pomodoro_time)
        break_timer(long_relax_time)


def pomodoro_timer(p_time):
    """Timer for work"""
    work_time = timedelta(minutes=int(p_time))
    while work_time:
        os.system("clear")
        spec_format = datetime.strptime(str(work_time), "%H:%M:%S")
        template = f'''
    Keep Calm and
    Just Work :)
    #############
    ### {spec_format.strftime('%M:%S')} ###
    #############'''
        print(template)
        work_time = work_time - timedelta(seconds=1)
        time.sleep(1)
    else:
        print('#' * 10000)
        time.sleep(5)


def break_timer(b_time):
    """Timer for relax"""
    relax_time = timedelta(minutes=int(b_time))
    while relax_time:
        os.system("clear")
        spec_format = datetime.strptime(str(relax_time), "%H:%M:%S")
        template = f'''
    Keep Calm and
    Just Rest :)
    #############
    ### {spec_format.strftime('%M:%S')} ###
    #############'''
        print(template)
        relax_time = relax_time - timedelta(seconds=1)
        time.sleep(1)
    else:
        print('#' * 10000)
        time.sleep(5)


if __name__ == '__main__':
    welcome()
    action = input("Please select one of the actions Pomodoro Timer (start/stop): ")
    main(action)

