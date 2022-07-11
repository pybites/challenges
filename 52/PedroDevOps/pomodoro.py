#!/usr/bin/env python3
"""
Author:  Pedro DevOps <pedroDevOps@gmail.com>
Purpose: Create my own Pomodoro Timer
Project: 100Days of code with Python
Progress: Round1, Day3 = R1D3
Challenge: https://codechalleng.es/challenges/52/
OBS:
    flake8 was used: # flake8 pomodoro.py
    autopep8 was used: # autopep8 --in-place --aggressive --aggressive pomodoro.py
    bandit was used: # bandit -r pomodoro.py
"""

from datetime import timedelta, datetime
from time import sleep
from os import system
import argparse


# Fuction that will do the countdown and print on terminal
def countdown(title, time_to_focus, time_to_rest):
    system('clear')
    stop_time = datetime.now() + time_to_focus
    resume_time = stop_time + time_to_rest

    # Loop for the focus time
    while datetime.now() < stop_time:
        delta = stop_time - datetime.now()
        totalMinute, second = divmod(delta.seconds, 60)
        hour, minute = divmod(totalMinute, 60)
        print(title, f"{hour}:{minute:02}:{second:02}", end='\r')
        sleep(1)

    print("Well done! Let's rest for: {}".format(time_to_rest))

    # Loop for the break time
    while datetime.now() < resume_time:
        delta = resume_time - datetime.now()
        totalMinute, second = divmod(delta.seconds, 60)
        hour, minute = divmod(totalMinute, 60)
        print(title, f"{hour}:{minute:02}:{second:02}", end='\r')
        sleep(1)
    system('clear')


def pomodoro_timer(title, interval_time, rest_time, how_many_cycles):
    keep_using_timer = True
    while keep_using_timer:
        try:
            i = 0
            while i < how_many_cycles:
                countdown((title + " Cycle " + str(i) + "-->"),
                          interval_time, rest_time)
                i = i + 1
            keep_using_timer = False
        except Exception:
            print("Something went wrong inside the pomodoro_timer function")
            break


# The Main Function
# Pass the args in the command line.
def main():
    parser = argparse.ArgumentParser(description='Pomodoro Timer')
    parser.add_argument(
        '-CH',
        '--cycle_hours',
        metavar='cycle_hours',
        default='0',
        help='how many hours to set the cycle timer')
    parser.add_argument(
        '-CM',
        '--cycle_minutes',
        metavar='cycle_minutes',
        default='0',
        help='how many minutes to set the cycle timer')
    parser.add_argument(
        '-CS',
        '--cycle_seconds',
        metavar='cycle_seconds',
        default='0',
        help='how many seconds to set the cycle timer')
    parser.add_argument(
        '-BH',
        '--break_hours',
        metavar='break_hours',
        default='0',
        help='how many hours to set the break timer')
    parser.add_argument(
        '-BM',
        '--break_minutes',
        metavar='break_minutes',
        default='0',
        help='how many minutes to set the break timer')
    parser.add_argument(
        '-BS',
        '--break_seconds',
        metavar='break_seconds',
        default='0',
        help='how many seconds to set the break timer')
    parser.add_argument('-HMC', '--how_many_cycles', metavar='how_many_cycles',
                        default='1', help='how many cycles')
    args = parser.parse_args()
    pomodoro_timer("Pomodoro ", timedelta(seconds=(int((args.cycle_hours) *
                                                       60 *
                                                       60) +
                                                   int((args.cycle_minutes) *
                                                       60) +
                                                   int(args.cycle_seconds))), timedelta(seconds=(int((args.break_hours) *
                                                                                                     60 *
                                                                                                     60) +
                                                                                                 int((args.break_minutes) *
                                                                                                     60) +
                                                                                                 int(args.break_seconds))), int(args.how_many_cycles))


if __name__ == "__main__":
    main()
