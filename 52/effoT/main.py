from datetime import datetime, timedelta
from time import sleep


def main(duration, reoccurance, pause_between):
    for i in range(reoccurance):
        timer(duration)
        sleep(pause_between)


def timer(delay):
    if type(delay) == int:
        start_time = datetime.today()
        alert_time = start_time + timedelta(0, delay)
        while True:
            current_time = datetime.today()
            if current_time >= alert_time:
                print("Times up {} seconds have passed, the timer was started at {} and now it's {}".format(
                    str(delay), str(start_time), str(current_time)))
                break
            sleep(1)
    else:
        print("The delay is in seconds and must be an integer")


def get_integer(msg):
    user_input = None
    while(type(user_input) != int):
        user_input = input(msg)
        try:
            user_input = int(user_input)
        except:
            pass
    return user_input


if __name__ == '__main__':
    duration = get_integer("For how many seconds do you want the timer to run? ")
    reoccurance = get_integer("For how many times do you want the timer to run? ")
    pause_between = get_integer("For how many seconds do you want the timer to pause between reoccurances? ")
    main(duration, reoccurance, pause_between)
