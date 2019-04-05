""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime as dt
from datetime import timedelta as td
from time import sleep


def pom_timer(work_time=25, break_time=5, rounds=1):
    for i in range(1, rounds + 1, 1):
        work_message = f'Round {i} of {rounds} Get to work! You can take a break at ' \
            f'{dt.now() + td(minutes=work_time): %X}'
        break_message = f'Great job. Take a {break_time} minute break. Work begins at' \
            f'{dt.now() + td(minutes=work_time) + td(minutes=break_time): %X}'
        done_message = f'Last round. Done for the day at {dt.now() + td(minutes=work_time): %X}'
        if i == rounds:
            print(done_message)
            sleep(work_time * 60)
            print('All Done - Enjoy your day!')
        else:
            print(work_message)
            sleep(work_time * 60)
            print(break_message)
            sleep(break_time * 60)

