# Py Bites challenge 52 - Create your own Pomodoro Timer
# https://codechalleng.es/challenges/52/

import argparse
import asyncio

parser = argparse.ArgumentParser(description='Pomodoro timer.')
parser.add_argument('time', metavar='N', type=int, default=1, help='time in units (e.g., 25)')
parser.add_argument('units', metavar='U', type=str, default='s', help='units of time: s=seconds, m=minutes. Default is minutes.')
args = parser.parse_args()
print(args)

desired_time = args.time
desired_units = args.units

def seconds_per_unit(units):
    """
    ==>> What?!? Python does not have a switch statement?!?   <<===
    params:
    units: "s" for seconds, "m" for minutes
    """
    seconds = 0
    if units == 's':
        seconds = 1
    if units == 'm':
        seconds = 60
    return seconds

async def main(time, units):
    total_seconds = time * seconds_per_unit(units)
    print("Starting pomodoro timer for {0} {1} ({2} seconds).".format(time, units, total_seconds))
    while total_seconds >= 0:
        await asyncio.sleep(1)
        print("{0} tick!".format(total_seconds))
        total_seconds -= 1

asyncio.run(main(desired_time, desired_units))

