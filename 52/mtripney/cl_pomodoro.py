#!/usr/bin/env python3
# Purpose: Terminal-based Pomodoro timer

from datetime import datetime
from datetime import timedelta
import argparse
import time


def countdown(minutes, beep):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        counter = f"{mins:02d}:{secs:02d}"
        # ASCII carriage return ("\r") sends cursor back to the start of the line
        print(counter, end="\r")
        # Pause a second...
        time.sleep(1)
        seconds -= 1
    if beep:
        # make a simple 'beep' sound with an ASCII bell ("\a")
        print("\a")
    print("Study over, time for a break!")


def display(args, current_time):
    finish_time = (datetime.now() + timedelta(minutes=args.study)).strftime("%H:%M")
    # A bell if alarm is on, a scored-through bell if it is off
    alarm_flag = "\U0001F514" if args.alarm else "\U0001F515"
    print(
        f"\n\U0001F345 It's {current_time} now. Study finishes at {finish_time} {alarm_flag}"
    )
    countdown(args.study, args.alarm)


def get_time():
    now = datetime.now()
    now_time = now.strftime("%H:%M")
    return now_time


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--alarm", action="store_true", help="'beep' when study period is over"
    )
    parser.add_argument("study", help="minutes in study period (integer)", type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    current_time = get_time()
    display(args, current_time)


if __name__ == "__main__":
    main()
