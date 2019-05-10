"""
pomodoro.py

This is my pomodoro app cli version

"""
from datetime import datetime
from datetime import timedelta
import time
import os


def main():
    """
    Main function
    """
    # clear the terminal at start
    os.system('cls' if os.name == 'nt' else 'clear')

    now = datetime.now()
    t = timedelta(minutes=1)
    remaining_seconds = t.seconds

    try:
        while remaining_seconds >= 1:
            print(f"{remaining_seconds // 60}")
            time.sleep(1)
            remaining_seconds -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
