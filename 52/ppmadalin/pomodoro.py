"""
pomodoro.py
"""
from datetime import timedelta
import time
import os


def countdown(seconds, message=None):
    """
    Countdown remainig time
    """
    while seconds >= 0:
        if message:
            print(message)
        print(f'{seconds // 60}:{seconds % 60}')
        time.sleep(1)
        seconds -= 1
        # clear prompt
        os.system('cls' if os.name == 'nt' else 'clear')

    return seconds


def main():
    """
    Main function
    """
    # clear the terminal at start
    os.system('cls' if os.name == 'nt' else 'clear')

    work = timedelta(minutes=1)
    break_time = timedelta(minutes=1)
    remaining_seconds = work.seconds

    try:
        while True:

            remaining_seconds = countdown(remaining_seconds, "Start working...")

            if remaining_seconds <= 0:
                break_remaining_seconds = countdown(break_time.seconds, "Take a break for 5 minutes...")
                remaining_seconds = work.seconds
                continue

    except KeyboardInterrupt:
        print("Bye..")


if __name__ == "__main__":
    main()
