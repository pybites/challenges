import time
from datetime import datetime
from datetime import timedelta

def timer(timer_type):
    if timer_type == "pomodoro":
        endtime = datetime.now() + timedelta(minutes=25)
    elif timer_type == "short_break":
        endtime = datetime.now() + timedelta(minutes=5)
    elif timer_type == "long_break":
        endtime = datetime.now() + timedelta(minutes=10)

    while (datetime.now().replace(microsecond=0) != endtime.replace(microsecond=0)):
        timeleft = endtime - datetime.now()
        timeleft = str(timeleft).split(".")[0]
        print(f"{timeleft}", end='\r')
        time.sleep(1)

    print(f"{timer_type} done!")
    return True

def main():
    pomodoro_count = 0
    while True:
        intervals = ["pomodoro", "break"]

        for timer_type in intervals:

            if timer_type == "pomodoro":
                pomodoro_count += 1
                print(f"It's work time! Pomodoro #{pomodoro_count}")

            if timer_type == "break":
                # determine whether it's a short or long break
                if pomodoro_count < 4:
                    # it's a short break
                    timer_type = "short_break"
                else:
                    timer_type = "long_break"
                    pomodoro_count = 0
                print(f"Starting {timer_type}!")

            timer(timer_type=timer_type)

if __name__ == "__main__":
    main()