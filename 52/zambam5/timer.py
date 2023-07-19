import platform

from datetime import datetime, timedelta
from time import sleep

if platform.system() == "Windows":
    from winsound import Beep


def pomodoro_timer(duration: int = 20, beep: bool = False):
    """
    Take a duration and begin a timer loop
    """
    duration_delta = timedelta(minutes=duration)
    d = datetime.now()
    d_ = d + duration_delta
    print("Starting timer " + str(d), "\r\nTimer will stop at " + str(d_))
    sleep(duration_delta.seconds)
    if beep:
        Beep(frequency=500, duration=50)
    pass


def main():
    if platform.system() == "Windows":
        b_question = input(
            'Do you want the timer to beep when finished? Answer "yes" or "no" '
        )
        if b_question == "no":
            beep = False
        else:
            beep = True
    else:
        beep = False
    while True:
        pomodoro_timer(beep=beep)
        again = input(
            'Do you want to start the timer again? Answer "yes" or "no" only '
        )
        if again == "yes":
            continue
        else:
            print("Ending the loop, hope you got some good work done!")
            sleep(0.5)
            break


if __name__ == "__main__":
    main()
