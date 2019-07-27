import argparse
import time
import os
from datetime import datetime, timedelta


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pomodoro Timer')
    parser.add_argument('--duration',
                        '-d',
                        dest='duration',
                        type=int,
                        help='Duration of the timer in minutes',
                        required=True)

    args = parser.parse_args()
    timer_duration = args.duration
    timer = timedelta(minutes=timer_duration)
    one_second = timedelta(seconds=1)

    i = 0
    print(timer.seconds)
    while i < timer.seconds:
        os.system("clear")
        print(timer)
        timer = timer - one_second
        i += 1
        time.sleep(1)

    print("Your timer is completed!")