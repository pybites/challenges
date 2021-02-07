from datetime import *
from time import sleep


class Task:
    def __init__(self):
        self.task_name = None
        self.is_task_completed = False
        self.total_task_duration = None
        self.total_break_duration = None
        self.section_working_timer = "NOT SET"
        self.section_break_timer = "NOT SET"

    def __init__(self, task_name, section_wirking_timer, section_break_timer):
        self.task_name = task_name
        self.is_task_completed = False
        self.total_task_duration = None
        self.total_break_duration = None
        self.section_working_timer = section_wirking_timer
        self.section_break_timer = section_break_timer

    def start_working_timer(self):
        expected_timer_end_time = datetime.today() + timedelta(seconds=self.section_working_timer)
        print(f"Your work session started. Duration {self.section_working_timer} minutes. Please concentrate on your '{self.task_name.upper()}' task.")

        self.wait_for_timer_ends(expected_timer_end_time)

        print("Your work session completed.")

    def start_break_timer(self):
        expected_timer_end_time = datetime.today() + timedelta(seconds=self.section_break_timer)
        print(f"Your break timer for '{self.task_name.upper()}' task started. Total duration {self.section_break_timer} minutes. Enjoy =)...")

        self.wait_for_timer_ends(expected_timer_end_time)

        print("Your break session completed.")

    def add_work_duration(self):

        session_duration = timedelta(seconds=self.section_working_timer)
        if self.total_task_duration is None:
            self.total_task_duration = session_duration
        else:
            self.total_task_duration = self.total_task_duration + session_duration

    def add_break_duration(self):
        session_duration = timedelta(seconds=self.section_break_timer)
        if self.total_break_duration is None:
            self.total_break_duration = session_duration
        else:
            self.total_break_duration = self.total_break_duration + session_duration

    @staticmethod
    def wait_for_timer_ends(amount_of_time_to_wait):
        while amount_of_time_to_wait >= datetime.today():
            sleep(1)