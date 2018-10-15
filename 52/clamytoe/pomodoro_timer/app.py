#!/usr/bin/env python3
"""
app.py

Pomodoro Timer
"""
import argparse
import datetime
from collections import namedtuple
from os import name, system
from sys import platform
from time import sleep
from typing import Any, ClassVar, List, Tuple

from .config import PLAYER, SOUNDS
from .log_init import setup_logging

logger: Any = setup_logging()
Params: Tuple[int, int, int] = namedtuple("Params", "duration breaks interval")


class Pomodoro:
    """Pomodoro Timer

    Given the amount of hours you want to spend on your task, it will prompt you to take a 5 minute break every 25
    minutes. At the end it sounds an alarm to let you know that the time that you specified is up.
    """

    MODES: ClassVar[List[str]] = "idle active respite".upper().split()

    def __init__(self, duration: int, breaks: int = 5, interval: int = 25) -> None:
        """Initializes the timer.

        :param duration: int - specifies how long the timer should run for, in hours.
        :param breaks:  int - specifies how long the breaks should be, in minutes.
        :param interval: int - specifies how long to work before taking a break, in minutes.
        """
        self.second: int = 1
        self.minute: int = self.second * 60
        self.hour: int = self.minute * 60
        self.duration: int = duration
        self.breaks: int = breaks
        self.interval: int = interval
        self.p_duration: int = self.duration * self.hour
        self.p_interval: int = self.interval * self.minute
        self.p_breaks: int = self.breaks * self.minute
        self.status: str = self.MODES[0]
        self.rounds: int = 1
        self.session_start: datetime.datetime = datetime.datetime.now()
        self.stop_time: datetime.datetime = self.session_start + datetime.timedelta(
            seconds=self.p_duration
        )

    def __repr__(self) -> str:
        """Representation of the object."""
        class_name: str = str(self.__class__).split(".")[-1].replace(">", "").replace(
            "'", ""
        )
        return f"{class_name}(duration:{self.duration} breaks={self.breaks} interval={self.interval})"

    def bye_message(self) -> None:
        """Exit message."""
        logger.info(f"{self.status}, session: end")
        print("Thanks for using clamytoe's Pomodoro Timer!")
        exit()

    def get_input(self) -> None:
        """Used to continue the program or quit it."""
        self.play("warning")
        key: str = input("Hit any key to continue, [q]uit: ")
        self.clear_screen()
        try:
            if key.lower() == "q":
                self.bye_message()
        except AttributeError:
            pass

        if self.status == "ACTIVE":
            self.play("break")
        else:
            self.play("begin")

    def pause(self, length: int) -> None:
        """Pauses the program execution for the desired length of time."""
        sleep(length)
        if self.status == "ACTIVE":
            print("Time for a break!")
        else:
            print("Time to get back to work!")
        self.get_input()

    def start(self) -> None:
        """Starts the timer."""
        start_time: datetime.datetime = datetime.datetime.now()
        self.stop_time = start_time + datetime.timedelta(seconds=self.p_duration)
        logger.info(f"{self.status}, session: start, projected: {self.stop_time}")
        self.clear_screen()
        print(
            f"Session ends approximately at: {str(self.stop_time).split('.')[0].split()[1]}"
        )
        self.start_timer()

    def start_break(self) -> None:
        """Starts the break."""
        work_time: datetime.datetime = datetime.datetime.now() + datetime.timedelta(
            seconds=self.p_breaks
        )
        if self.rounds % 4 == 0:
            self.start_extended_break(work_time)
        else:
            print("Go stretch your legs and get some water.")
            print(f"Start again at: {str(work_time).split('.')[0].split()[1]}")
            self.status = self.MODES[2]
            logger.info(f"{self.status}, break_until: {work_time}")

    def start_extended_break(self, work_time):
        extended = 10 * self.minute
        work_time += datetime.timedelta(seconds=extended)
        print("Time for an extended break!")
        print(f"Start again at: {str(work_time).split('.')[0].split()[1]}")
        self.status = self.MODES[2]
        logger.info(f"{self.status}, break_until: {work_time}")

    def start_interval(self) -> None:
        """Starts the interval timer."""
        break_time: datetime.datetime = datetime.datetime.now() + datetime.timedelta(
            seconds=self.p_interval
        )
        print(
            f"[{self.rounds}] Next break at: {str(break_time).split('.')[0].split()[1]}"
        )
        self.rounds += 1
        if self.status == "IDLE":
            self.play("begin")
        self.status = self.MODES[1]
        logger.info(f"{self.status}, interval: {self.rounds}")

    def start_timer(self) -> None:
        """Initiates the timing cycle."""
        try:
            while datetime.datetime.now() < self.stop_time:
                if self.rounds == 8:
                    self.clear_screen()
                    print("Nicely done! You've completed this session!.")
                    self.play("done")
                    self.rounds = 0
                    self.status = self.MODES[0]
                    logger.info(f"{self.status}, intervals: completed")
                    # self.get_input()
                    exit()
                else:
                    self.start_interval()
                    self.pause(self.p_interval)
                    self.start_break()
                    self.pause(self.p_breaks)
            self.clear_screen()
            print("Nice, you're all done!.")
            self.play("done")
            self.bye_message()
        except KeyboardInterrupt:
            self.clear_screen()
            logger.info("User terminated session.")
            print("Timer stopped by the user.")

    @staticmethod
    def clear_screen() -> None:
        """
        Clears the screen
        :return: None
        """
        _: int = system("cls" if name == "nt" else "clear")

    @staticmethod
    def play(sound: str) -> None:
        """Plays the sound file.

        :param sound: str - the path and name of the sound file to play
        :return: None
        """
        logger.info(f"sound: {PLAYER} {SOUNDS[sound]}")
        system(f"{PLAYER} {SOUNDS.get(sound, SOUNDS['warning'])}")


def get_args() -> Params:
    """Argument parser."""
    parser = argparse.ArgumentParser(description="Pomodoro Productivity Timer")
    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        help="How long you going to work for, in hours",
        required=False,
    )
    parser.add_argument(
        "-b", "--breaks", type=int, help="How long the breaks should be", required=False
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        help="Minutes to work before taking a break",
        required=False,
    )
    args = parser.parse_args()
    duration: int = args.duration
    breaks: int = args.breaks
    interval: int = args.interval
    params: Params = Params(duration=duration, breaks=breaks, interval=interval)
    logger.info(f"Parsed parameters: {params}")
    return params


def main() -> None:
    """Main entry point of the application."""
    if platform != "linux":
        logger.warning(f"Attempted to run on unsupported {platform} platform.")
        print(f"Sorry, your platform {platform} is not supported!")
        exit(1)

    params: Params = get_args()

    duration: int = params.duration if params.duration else 4
    breaks: int = params.breaks if params.breaks else 5
    interval: int = params.interval if params.interval else 25

    timer: Pomodoro = Pomodoro(duration, breaks=breaks, interval=interval)
    logger.info(f"Initialize Session: {repr(timer)}")
    timer.start()


if __name__ == "__main__":
    main()
