# Py Bites challenge 52 - Create your own Pomodoro Timer
# https://codechalleng.es/challenges/52/

# Example usages:
#   python3 pomodoro.py --time 5 --units s
#   python3 pomodoro.py --time 25 --units m
#   python3 pomodoro.py

import argparse
import asyncio
import sys
from datetime import timedelta

if sys.platform == 'win32':
    import winsound

def handle_args():
    """
    Processes the user arguments.
    :time: Optional. Integer number representing time in the unit of measurement. Defaults to 10.
    :unit: Optional. String representing the unit of time accompanying the time parameter. Defaults to 's' (seconds).
    """
    parser = argparse.ArgumentParser(description='Pomodoro timer.')
    parser.add_argument('--time', type=int, default=10, help='time in units (e.g., 25). Default is 10.')
    parser.add_argument('--units', type=str, default='s', help='units of time: s=seconds, m=minutes. Default is s.')
    args = parser.parse_args()
    print(args)
    return args

def seconds_per_unit(units):
    """
    Converts units to seconds.
    :units: "s" for seconds, "m" for minutes
    """
    seconds = 0
    if units == 's':
        seconds = 1
    if units == 'm':
        seconds = 60
    return seconds

async def pomodoro(time=10, units='s'):
    """
    The core pomodoro timer code.
    It displays a countdown timer, ticking down every second.
    When finished, it "beeps" and displays a completion message.
    This timer can only handle one time and one unit.
    :time:   integer number for the duration of the timer, in units.
    :units:  "s" for seconds, "m" for minutes
    """
    total_seconds = time * seconds_per_unit(units)
    print("Starting pomodoro timer for {0}{1}.".format(time, units))
    while total_seconds > 0:
        await asyncio.sleep(1)
        td = str(timedelta(seconds=total_seconds))
        print("\r{0}".format(td), end='')
        total_seconds -= 1

# Process user arguments.
args = handle_args()
desired_time = args.time
desired_units = args.units

# Run the pomodoro timer.
asyncio.run( pomodoro(desired_time, desired_units) )

# Final messages and "beep".
print("\rDING! Pomodoro time {0}{1} has finished".format(desired_time, desired_units))
if sys.platform == 'win32':
    winsound.Beep(2000,1000)   #2000 is the frequency in Hz, 1000 is the duration in ms
else:
    print('\a')   #UNTESTED