""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime, timedelta
import time
import signal
import sys

STEP_INTERVAL = 10

def signal_handler(sig, frame):
    print('good bye!')
    sys.exit(0)

def pomodoro(work_interval=20, rest_interval=5):
    begin = datetime.now()
    work = timedelta(minutes=work_interval)
    rest = timedelta(minutes=rest_interval)
    while True:
        while True:
            elapsed_time = datetime.now() - begin
            print(f"working for minutes: {round(elapsed_time.seconds/60,0)} seconds: {elapsed_time.seconds}")
            if elapsed_time >= work:
                break
            time.sleep(STEP_INTERVAL)
        while True:
            elapsed_time = datetime.now() - begin
            print(f"resting for minutes: {round(elapsed_time.seconds/60,0)} seconds: {elapsed_time.seconds}")
            if elapsed_time >= rest:
                break
            time.sleep(STEP_INTERVAL)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    pomodoro()



