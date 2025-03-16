import time
import argparse
from datetime import datetime
from datetime import timedelta

DEFAULT_POMODORO_TIME = 25
DEFAULT_BREAK_TIME = 5

def pomodoro_timer(duration):
    print("Starting timer for %s..." % str(duration))
    while(duration.total_seconds() > 0):
        minutes = duration.total_seconds() / 60
        print("Still %s minutes before the end of the timer" % minutes)
        time.sleep(60)
        duration = duration - timedelta(minutes=1)
    print("The timer finished")

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="The name of the user")
parser.add_argument("-p", "--pomodoro",
    type=int,
    help="The pomodoro duration in minutes",
    default=DEFAULT_POMODORO_TIME,
    dest="pomodoro_value")
parser.add_argument("-b", "--break",
    type=int,
    help="The break duration in minutes",
    default=DEFAULT_BREAK_TIME,
    dest="break_value")
args = parser.parse_args()

if args.name:
    print("Hello %s, we start your pomodoro timer!" % args.name)

while(True):
    print("POMODORO!")
    pomodoro_timer(timedelta(minutes=args.pomodoro_value))
    print("BREAK!")
    pomodoro_timer(timedelta(minutes=args.break_value))
