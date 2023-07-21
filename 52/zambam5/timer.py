import platform

from datetime import datetime, timedelta
from time import sleep

if platform.system() == "Windows":
    from winsound import Beep


def pomodoro_timer(minutes: int = 20, beep: bool = False) -> None:
    """
    Take a duration in minutes and sleep for that amount of time
    """
    minutes_delta = timedelta(minutes=minutes)
    date_now = datetime.now()
    date_after_minutes = date_now + minutes_delta
    print(
        "Starting timer " + str(date_now),
        "\r\nTimer will stop at " + str(date_after_minutes),
    )
    sleep(minutes_delta.seconds)
    if beep and platform.system() == "Windows":
        Beep(frequency=500, duration=50)
    pass


def main() -> None:
    if platform.system() == "Windows":
        beep = False
        b_question = input(
            'Do you want the timer to beep when finished? Answer "yes" or "no" '
        )
        if b_question == "no":
            beep = True
    else:
        beep = False
    while True:
        pomodoro_timer(beep=beep)
        again = input(
            'Do you want to start the timer again? Answer "yes" or "no" only '
        )
        if again == "no":
            print("Ending the loop, hope you got some good work done!")
            sleep(0.5)
            break


if __name__ == "__main__":
    main()
