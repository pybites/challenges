"""
A simple countdown script.
"""
from datetime import datetime, date, timedelta


def time_until(date):
    today = date.today()
    return (date - today).days


def get_event():
    event = input("Name of the event: ")
    return event


def get_date():
    date = input("Date of the event (yyyy mm dd)")
    return datetime.strptime(date, '%Y %m %d').date()


def print_instructions():
    print("------------------------------")
    print("          TIME UNTIL          ")
    print("------------------------------")
    print()
    print("Enter an event and date to know how many days you \n",
          "have to wait until it happens :)\n")
    print("Enter your event.\n")
    print("Exemple:")
    print("\t Event = Christmas")
    print("\t Date = 2019 12 25\n\n")


def message(event, days):
    if days < 0:
        print(f'{event.title()} was {-days} days ago!')
    elif days == 1:
        print(f'{event.title()} is tomorrow!')
    elif days == 0:
        print(f'{event.title()} is today!')
    else:
        print(f'There is {days} days to wait until {event}.')  


def main():
    print_instructions()
    event = get_event()
    print(event)
    date = get_date()
    days = time_until(date)
    message(event, days)


if __name__ == "__main__":
    main()
