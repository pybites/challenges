import argparse
import datetime
import time
import sys

TIMER_END = datetime.timedelta(minutes=0)


def countdown(timer_minutes=20):
    timer = datetime.timedelta(minutes=timer_minutes)
    while timer != TIMER_END:
        print(timer, end='\r', flush=True)
        timer -= datetime.timedelta(seconds=1)
        time.sleep(1)

    print(TIMER_END)
    print('Pomodoro completed! Time for a break...')


def parse_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '--timer_minutes',
        help='duration in minutes of timer (default is 20)',
        type=int,
        default=20
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    countdown(args.timer_minutes)
