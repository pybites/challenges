""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime, timedelta


def timer(user_input):
    work_start = datetime.now()
    time_interval = timedelta(seconds=user_input)

    work_stop = work_start + time_interval

    print(f'Session start ---> {work_start}')
    print(f'Session end ---> {work_stop}')

    return work_stop


def main():
    print('--------------------------------------')
    print('     Cocktail Pomodoro Timer')
    print('--------------------------------------')

    work_session_duration = int(input('Select work session duration: '))
    work_stop = timer(work_session_duration)
    now = datetime.now()
    stop = False

    while not stop:
        time_now = datetime.now()
        time_now_display = time_now.strftime('%H:%M:%S')
        print(time_now_display)
        if time_now >= work_stop:
            print('Work finished!')
            stop = True


if __name__ == '__main__':
    main()
