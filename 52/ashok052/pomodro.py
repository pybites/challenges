""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime
from time import sleep

DEFAULT_WORK_IN_MINS = 20
DEFAULT_BREAK_IN_MINS = 5
MAX_COUNT_TIMER = 5


class Timer():

    def __init__(self, work=DEFAULT_WORK_IN_MINS, rest=DEFAULT_BREAK_IN_MINS):
        self.work = work
        self.rest = rest
        self.count = 0

    def startTimer(self):
        while self.count < 5:
            now = datetime.now()
            print(f'Starting timer for {self.work} minutes at {now}')
            sleep(self.work * 60)
            if (self.count == 4):
                break
            print(
                f'Great Job !!\nLet\'s take a break now for {self.rest} minutes')
            sleep(self.rest * 60)
            self.count += 1
            print('Let\'s get started again !!')

        if self.count == 4:
            print('Let\'s go to bed now, Worked too much for today')
            return


def main():
    work = int(input("Enter the work time in mins: "))
    rest = int(input("Enter the break time in mins: "))
    inst = Timer(work, rest)
    inst.startTimer()


if __name__ == "__main__":
    main()
