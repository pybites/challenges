from datetime import timedelta
import time

def print_header():
    print("------------------------------")
    print("     Pomodoro Timer App")
    print("------------------------------")
    print()

def user_choice():
    choice = input("Choose one of the following:"
                    " [1] Pomodoro 25min"
                    " [2] Short break 5min"
                    " [3] Long break 10min"
                    " [4] Exit: ")
    if choice == "1":
        pomodoro()
    elif choice == "2":
        short_break()
    elif choice == "3":
        long_break()
    elif choice == "4":
        quit
    else:
        print("Please enter a valid choice: ")


def pomodoro():
    timer = timedelta(minutes=25)
    while timer:
        print(f"Pomodoro time remaining {str(timer)}")
        time.sleep(1)
        timer -= timedelta(seconds=1)
    print("Pomodoro: Time is up!")


def short_break():
    timer = timedelta(minutes=5)
    while timer:
        print(f"Short break time remaining {str(timer)}")
        time.sleep(1)
        timer -= timedelta(seconds=1)
    print("Short Break: Time is up!")


def long_break():
    timer = timedelta(minutes=10)
    while timer:
        print(f"Long break time remaining {str(timer)}")
        time.sleep(1)
        timer -= timedelta(seconds=1)
    print("Long Break: Time is up!")


def main():
    print_header()
    user_choice()

main()