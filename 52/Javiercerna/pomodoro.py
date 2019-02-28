import argparse
import datetime
import time
import sys

TIMER_END = datetime.timedelta(minutes=0)


def countdown(timer_minutes, end_message):
    timer = datetime.timedelta(minutes=timer_minutes)
    while timer != TIMER_END:
        print(timer, end='\r', flush=True)
        timer -= datetime.timedelta(seconds=1)
        time.sleep(1)

    print(TIMER_END)
    print(end_message)


def parse_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '--timer_minutes',
        help='duration in minutes of timer (default is 20)',
        type=int,
        default=20
    )

    parser.add_argument(
        '--break_minutes',
        help='duration in minutes of each break (default is 5)',
        type=int,
        default=5
    )

    parser.add_argument(
        '--timer_cycles',
        help='Cycles of timer and break (default is 1)',
        type=int,
        default=1
    )

    return parser.parse_args()


if __name__ == '__main__':
    timer_end_msg = 'Pomodoro completed! Time for a break...'
    break_end_msg = 'Break finished! Let\'s continue...'
    args = parse_arguments()

    for cycle in range(args.timer_cycles):
        print(f'Starting cycle {cycle+1}/{args.timer_cycles}')
        countdown(args.timer_minutes, timer_end_msg)
        countdown(args.break_minutes, break_end_msg)
