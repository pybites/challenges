"""
pomodoro.py
"""

import sys
import argparse
from time import sleep
from datetime import datetime, date, timedelta


BREAK_URL = "https://www.youtube.com/watch?v=fDvDC5yNn6M"
DEFAULT_POMODORO_DURATION = 25 # minutes 
DEFAULT_BREAK_DURATION = 2 # minutes 
DEFAULT_POMODORO_COUNT = 5


def log(msg):
    timestamp = datetime.today()
    print(f"[{timestamp}] {msg}")


def video_break():
    import webbrowser
    webbrowser.open_new_tab(BREAK_URL)


def take_break(duration):
    log("Time for break!")
    video_break()
    sleep(duration)


def start(minutes=DEFAULT_POMODORO_DURATION, break_duration=DEFAULT_BREAK_DURATION):
    eta = timedelta(minutes=minutes)
    current_time = datetime.today()

    log(f"Starting timer for {minutes} minute[s] duration...")
    log(f"Breaking at around {current_time + eta}.")
    sleep(eta.total_seconds())

    break_duration = timedelta(minutes=break_duration).total_seconds()
    take_break(duration=break_duration)
    print("\n")


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-m", 
        "--minutes",
        help="pomodoro duration in minutes.",
        type=int,
        default=DEFAULT_POMODORO_DURATION
    )
    ap.add_argument(
        "-c",
        "--count",
        help="number of pomodoros.",
        type=int,
        default=DEFAULT_POMODORO_COUNT
    )
    ap.add_argument(
        "-b",
        "--break-time",
        help="duration of break time in minutes.",
        type=int,
        default=DEFAULT_BREAK_DURATION
    )
    args = vars(ap.parse_args())
        
    minutes = args.get("minutes", DEFAULT_POMODORO_DURATION)
    pomo_count = args.get("count", DEFAULT_POMODORO_COUNT)
    break_duration = args.get("break_time", DEFAULT_BREAK_DURATION)
    print(f"starting {pomo_count} Pomodoro[s] of {minutes} minute[s] each with a break duration of {break_duration} minute[s]"
        .upper())
    print("\n\n")
         
    while pomo_count:
        start(minutes=minutes, break_duration=break_duration)
        pomo_count -= 1


if __name__ == "__main__":
    print("---------------------------------------------------------")
    print("                        POMODORO TIMER                   ")
    print("---------------------------------------------------------")
    main()