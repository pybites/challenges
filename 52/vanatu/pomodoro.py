from datetime import datetime, timedelta
import time


POMODORO = 25
BREAK = 5


def main():
    while True:
        user_choice = input(f'''Pomodoro time is {POMODORO} min. Break time is {BREAK} min. Long break is {3*BREAK} min.
1 - start pomodoro
0 - change timers
> ''')
        if user_choice == '1':
            print('start pomodoro')
            t = datetime.strptime(str(POMODORO), '%M')
            while t.strftime('%M:%S') != '00:00':
                print(t.strftime('%M:%S'))
                t -= timedelta(seconds=1)
                time.sleep(1)


if __name__ == '__main__':
    main()
