"""
A simple command line based Pomodoro timer. Timer duration and break duration can be passed as arguments, but are
optional. Default timer value is set as 25 minutes. Default break duration is set as 0 minutes.
The timer is defined as a class for reuse.

Note: Please pip install 'colorama' pacakge as this is used to color the output.
"""

from datetime import datetime, timedelta
import time
import sys
import argparse
from colorama import Fore
import itertools

NOTIFICATION_COUNT = 5
SECONDS = 60
DEFAULT_POMODORO_DURATION = 25
DEFAULT_BREAK_DURATION = 0


class PomodoroTimer:

    def __init__(self, work_duration, break_duration):
        self.work_minutes = work_duration
        self.break_minutes = break_duration

    def start_timer(self):

        td = td_duration = timedelta(minutes=self.work_minutes)
        timer = datetime.now().replace(microsecond=0) + td
        timedelta_1s = timedelta(seconds=1)
        timer_loop = True

        timer_msgs1 = itertools.cycle(['Timer expired!', ' '])

        # Timer loop
        while timer_loop:
            # Print the timer
            sys.stdout.write(Fore.BLUE + f'\r {int(td.seconds/60):02}:{(td.seconds % 60):02}')
            sys.stdout.flush()

            td -= timedelta_1s
            time.sleep(1)

            # Check if timer expired
            if timer.time() <= datetime.now().replace(microsecond=0).time():
                # If break duration is given, print a message and sleep for <break duration>
                if self.break_minutes:
                    sys.stdout.write(Fore.YELLOW + f'\r Timer expired!. Take a break for {self.break_minutes} minute(s)')
                    sys.stdout.flush()
                    time.sleep(self.break_minutes * SECONDS)
                    td = td_duration
                    timer = datetime.now().replace(microsecond=0) + td
                else:
                    # If no break duration, notify the user and exit.
                    timer_loop = False

                    for i in range(NOTIFICATION_COUNT):
                        sys.stdout.write(Fore.RED + '\r' + next(timer_msgs1))
                        sys.stdout.flush()
                        time.sleep(1)


def main():

    # Using argparse module to define and parse arguments
    parser = argparse.ArgumentParser(description="Pomodoro timer.")
    parser.add_argument('-w', action='store', type=int, default=DEFAULT_POMODORO_DURATION)
    parser.add_argument('-b', action='store', type=int, default=DEFAULT_BREAK_DURATION)
    args = parser.parse_args()

    # Create the timer instance and start the timer
    pt = PomodoroTimer(args.w, args.b)
    pt.start_timer()


if __name__ == '__main__':
    main()

