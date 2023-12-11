import argparse
import os
from time import sleep
from datetime import timedelta, time, datetime


class Pomodoro:
    def __init__(self, session_interval, break_interval, learning_sessions):
        self.session_interval = session_interval
        self.break_interval = break_interval
        self.learning_sessions = learning_sessions
        self.session_number = 1

    def start_pomodoro(self):
        for session in range(self.learning_sessions):
            os.system('clear')
            start_time = datetime.now()
            finish_time = start_time + timedelta(minutes=self.session_interval)
            print(f"Starting pomodoro session: {self.session_number}, "
                  f"\nstart time: {start_time} \nbreak_time: {finish_time}")
            self.sleep_given_minutes_and_count_every_single_minute(self.session_interval)
            if self.session_number < self.learning_sessions:
                self.start_break()
            self.session_number += 1
        print("Good work you finished your all set pomodoro sessions")

    def start_break(self):
        os.system('clear')
        start_time = datetime.now()
        finish_time = start_time + timedelta(minutes=self.break_interval)
        print(f"Starting pomodoro break:"
              f"\nstart time: {start_time} \nbreak_time: {finish_time}")
        self.sleep_given_minutes_and_count_every_single_minute(self.break_interval)

    @staticmethod
    def sleep_given_minutes_and_count_every_single_minute(minutes_to_sleep):
        for minute in range(minutes_to_sleep):
            print(f"Remaining minutes: {time(minute=minutes_to_sleep)}")
            sleep(60)
            minutes_to_sleep -= 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Pomodoro',
        description='Simple Pomodoro CLI')
    parser.add_argument('-s', '--session_interval', help="Session Interval in minutes", type=int, required=True)
    parser.add_argument('-b', '--break_interval', help="Break Interval in minutes", type=int, required=True)
    parser.add_argument('-n', '--session_number', help="Sessions number", type=int, required=True)

    args = parser.parse_args()
    pomodoro = Pomodoro(args.session_interval, args.break_interval, args.session_number)
    pomodoro.start_pomodoro()
