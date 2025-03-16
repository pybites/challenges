from datetime import datetime, timedelta
import winsound
import time


def beep():
    frequency = 2500
    duration = 100
    for i in range(4):
        winsound.Beep(frequency, duration)
        time.sleep(0.00001)


def decrement(time_wait: timedelta) -> timedelta:
    return time_wait - timedelta(seconds=1)


def status(flg: int) -> None:
    if flg:
        return "break time", 0

    else:
        return "pomodoro", 1


def countdown(time_p: timedelta, st)-> None:
    while time_p > timedelta(seconds=0):
        time_p = decrement(time_p)
        print(st, ":", time_p, end="\r", flush=True)
        time.sleep(1)


if __name__ == "__main__":
    time_wait = float(input("Duration in minutes: "))
    print('CRTL+C to stop')
    time_p = timedelta(minutes=time_wait)

    start = True
    flg = 0
    try:
        while start:
            st, flg = status(flg)
            countdown(time_p, st)
            beep()
    except KeyboardInterrupt:
        print("\nIt is the end")
