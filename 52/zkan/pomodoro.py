""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import timedelta
import time


input_minutes = input('Set the duration (mins): ')
duration = int(input_minutes) * 60
while True:
    print(timedelta(seconds=duration))
    duration -= 1
    if duration < 0:
        break

    time.sleep(1)

print('Time\'s Up')
