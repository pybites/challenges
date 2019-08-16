""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime, timedelta
import winsound


def beep():
    winsound.Beep(4000, 100)


class Pomodoro:

    def __init__(self, duration):
        self.duration = timedelta(seconds=duration*60)
        self.paused_state = True
        self.start_time: datetime

    def start_timer(self):
        self.start_time = datetime.now()
        self.paused_state = False

    def pause(self):
        if self.paused_state:
            print('resume')
            self.start_timer()
            self.paused_state = False
        else:
            print('pause')
            self.update_duration()
            self.paused_state = True

    def update_duration(self):
        if not self.paused_state:
            self.duration -= (datetime.now() - self.start_time)
            if not self.check_expired():
                self.start_timer()

    def check_expired(self):
        if self.duration.days < 0:
            beep()
            exit()
        return self.duration.days < 0

    def __repr__(self):
        self.update_duration()
        return str(self.duration)


if __name__ == '__main__':

    user_input = int(input('Enter total time in minutes: '))
    pomodoro = Pomodoro(user_input)
    while True:
        user_input = input('(s)tart, (p)ause, (d)isplay, (e)xit: ')
        if user_input == 's':
            pomodoro.start_timer()
        elif user_input == 'p':
            pomodoro.pause()
        elif user_input == 'd':
            print(pomodoro)
        else:
            print(pomodoro)
            exit()
