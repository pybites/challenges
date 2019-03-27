""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime, timedelta
from decimal import *
import time
import signal
import sys

def signal_handler(sig, frame):
    print('good bye!')
    sys.exit(0)

def pomodoro(work_interval=20, rest_interval=5, step_interval=60):
    work = timedelta(minutes=work_interval)
    rest = timedelta(minutes=rest_interval)
    interval = work
    todo = "working"
    while True:
        begin = datetime.now()
        while True:
            elapsed_time = datetime.now() - begin
            elapsed_minutes = Decimal(elapsed_time.seconds / 60).quantize(Decimal('1.'), rounding=ROUND_DOWN)
            print(f"{todo} for minutes: {elapsed_minutes} seconds: {elapsed_time.seconds}")
            if elapsed_time >= work:
                break
            time.sleep(step_interval)
        todo, interval = ("resting", rest) if todo == "working" else ("working", work)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    pomodoro(1,1,5)



