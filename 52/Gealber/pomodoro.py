import argparse
import time
from datetime import datetime, timedelta


def user_input():
    parser = argparse.ArgumentParser(prog="pomodoro",
                                     allow_abbrev=False,
                                     usage="%(prog)s [options] time",
                                     description="Set a time to be full concentrate",
                                     epilog="Have fun :)..!!")
    parser.add_argument("work",
                        help="Time in mm:ss format that it is gonna be set",
                        type=str)
    parser.add_argument('-l',
                        '--loop',
                        help="The loop to be set of the pomodoro and the break time",
                        default=['1', '05:00'],
                        type=str,
                        nargs=2)
    args = parser.parse_args()
    time_off = args.work
    loop = args.loop
    return time_off, loop


def process_time(time):
    d = datetime.strptime(time, '%M:%S')
    minutes, secs = d.minute, d.second
    return minutes, secs


def set_pomodoro(d, break_time, loop_length):
    working_time = timedelta(minutes=d[0], seconds=d[1])
    resting_time = timedelta(minutes=break_time[0],
                             seconds=break_time[1])
    for _ in range(loop_length):
        starting_time = datetime.now()
        while True:
            elapsed_time = datetime.now() - starting_time
            print(
                f'Focused during: {elapsed_time.seconds // 60}:{elapsed_time.seconds % 60}!!')
            if elapsed_time > working_time:
                break
            time.sleep(60)
        print(
            f"Resting time: {resting_time.seconds // 60}:{resting_time.seconds % 60}")
        time.sleep(resting_time.total_seconds())


def main():    
    time_off, loop = user_input()
    d = process_time(time_off)
    break_time = process_time(loop[1])
    loop_length = int(loop[0])
    set_pomodoro(d, break_time, loop_length)


if __name__ == "__main__":
    main()
