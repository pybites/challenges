from datetime import datetime, timedelta
from time import sleep
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def timer(duration: timedelta, state_name: str,
          start_time: datetime = None):
    if start_time is None:
        start_time = datetime.now()
    while (datetime.now() < start_time + duration):
        cls()
        now = datetime.now()
        print(f"In {state_name}..")
        print(f"Current Time is {now}")
        print(f"{state_name} ends at {start_time + duration}")
        print(f"Time left: {start_time + duration - now}")
        print("^C to quit")
        sleep(1)


def start_pomodoro(pomodoro_delta: timedelta, break_delta: timedelta):
    in_pomodoro_state = True
    while 1:
        if in_pomodoro_state:
            timer(duration=pomodoro_delta, state_name="Pomodoro")
        else:
            timer(duration=break_delta, state_name="Break")
        in_pomodoro_state = not(in_pomodoro_state)


pomodoro_minutes = int(input("Enter your Pomodoro Time in minutes: "))
pomodoro_timedelta = timedelta(minutes=pomodoro_minutes)

break_minutes = int(input("Enter your Break Time in minutes: "))
break_timedelta = timedelta(minutes=break_minutes)

start_pomodoro(pomodoro_timedelta, break_timedelta)
