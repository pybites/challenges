"""
Very simple pomodoro application, you can choose pomodoro duration, break length and how many times you want to repeat
process, to start application you need to install speech dispatcher, you can use command:
sudo apt install speech-dispatcher
Enjoy!
"""

import argparse
from datetime import datetime, timedelta
import time
import os
import sys

# making arg parse arguments with the default values
parser = argparse.ArgumentParser()
parser.add_argument(
    "--duration",
    help="length of the pomodoro duration in minutes, default value is 20",
    type=int,
    default=20
)
parser.add_argument(
    '--count',
    help='how many pomodoros you want to do',
    type=int,
    default=4
)
parser.add_argument(
    '--br_length',
    help='length of the break in minutes',
    type=int,
    default=5
)
args = parser.parse_args()
duration = args.duration
break_length = args.br_length
iteration_count = args.count
print(args.duration, args.br_length, args.count)

# function which makes small animations which shows to user that application is working all the time
def animation(i):
    animation = "|/-\\"
    time.sleep (0.2)
    sys.stdout.write("\r" + animation[i % len (animation)])
    sys.stdout.flush()

# timer for break duration with specific outputs for break
def break_timer(break_length, start_time):
    # speech-dispatcher
    os.system ('spd-say "break"')
    sys.stdout.write("\n break started at: {} and should end at: {}".format (
        datetime.now(), datetime.now () + timedelta (minutes=break_length)))
    timer = True
    i = 0
    while timer:
        work_duration = datetime.now() - start_time
        animation(i)
        i += 1
        if work_duration >= timedelta(minutes=break_length):
            timer = False

# timer for pomodoro duration with specific outputs for pomodoro
def pomodoro_timer(pomodoro_duration, start_time):
    # speech-dispatcher
    os.system ('spd-say "time to work"')
    sys.stdout.write("\n pomodoro started at: {} and will end at: {}".format (
        datetime.now(), datetime.now () + timedelta(minutes=duration)))
    timer = True
    i = 0
    while timer:
        work_duration = datetime.now() - start_time
        animation(i)
        i += 1
        if work_duration >= timedelta(minutes=pomodoro_duration):
            timer = False

# main function which uses timers in for loop which is in rango of iteration count choosen by user, or default one
def main():
    for pomodoro_iteration in range(iteration_count):
        # there will be different behaviours for first and last iteration
        if pomodoro_iteration == 0:
            sys.stdout.write ("""\n pomodoro started with the following configuration: \n
                                    length of one pomodoro iteration: {} min\n
                                    break length: {} min\n
                                    number of iterations: {}\n""".format (duration, break_length,
                                                                          iteration_count))
            pomodoro_timer(duration, datetime.now())
            break_timer(break_length, datetime.now())
        elif pomodoro_iteration == iteration_count - 1:
            pomodoro_timer(duration, datetime.now())
        else:
            pomodoro_timer(duration, datetime.now())
            break_timer(break_length, datetime.now())
    # speech-dispatcher
    os.system ('spd-say "thats it good job"')


if __name__ == '__main__':
    main()