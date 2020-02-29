from datetime import datetime, timedelta
import time


TIMERS = {'1': ['Pomodoro', 25], '2': ['Break', 5], '3': ['Long Break', 15]}


def main():
    while True:
        for k, v in TIMERS.items():
            print(f'{k} - start {v[0]} ({v[1]} min.)')
        print('0 - Exit')
        user_choice = input('> ')

        if user_choice == '0':
            break
        elif user_choice in TIMERS:
            t = datetime.strptime(str(TIMERS[user_choice][1]), '%M')
            while t.strftime('%M:%S') != '00:00':
                print(f"{TIMERS[user_choice][0]} > {t.strftime('%M:%S')}")
                t -= timedelta(seconds=1)
                time.sleep(1)


if __name__ == '__main__':
    main()
