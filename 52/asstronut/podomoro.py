from datetime import datetime, timedelta
import time

def podomoro_timer(cycles, focus_time, break_time):
    cycles = cycles
    one_second = timedelta(seconds=1)

    while True:
        print('Focus time!')
        focus = timedelta(minutes=focus_time)  # input
        t_break = timedelta(minutes=break_time)   # input
        while focus > timedelta(seconds=0):
            focus -= one_second
            print(focus)
            time.sleep(1)
        cycles -= 1
        if cycles == 0:
            break
        print('Break time!')
        while t_break > timedelta(seconds=0):
            t_break -= one_second
            print(t_break)
            time.sleep(1)

if __name__ == '__main__':
    cycles = int(input('Mau waktu fokus berapa kali? '))
    focus_time = int(input('Mau fokus berapa menit? '))
    break_time = int(input('Mau waktu istirahat berapa menit? '))
    podomoro_timer(cycles=cycles, focus_time=focus_time, break_time=break_time)