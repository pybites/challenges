import sqlite3
import sys

db = sqlite3.connect('inventory.db')


def welcome():
    """Start the inventory program."""
    print("ROOM INVENTORY AND VALUATION".center(80))
    print("-".center(80, '-'))
    display_menu()


def display_menu():
    """Display the menu of options for the user."""
    r = input("""What would you like to do? (Choose an option)
    * (U)pdate room inventory
    * (A)dd a new room
    * (P)rint room inventory
    * (E)nd Inventory Program
    """)
    if str(r.lower()) not in ['u', 'a', 'p', 'e']:
        print("That is not a valid option.")
        display_menu()
    elif r.lower() == 'u':
        update_room()
    elif r.lower() == 'a':
        add_room()
    elif r.lower() == 'p':
        print_inventory()
    elif r.lower() == 'e':
        sys.exit()
    else:
        raise ValueError


def update_room():
    """Update the room inventory."""
    pass


def add_room():
    """Add a new room to the database."""
    print("ADD A ROOM".center(80))
    print("-".center(80, '-'))
    room = str(_get_room_name())
    db.execute('INSERT into room (name) VALUES (?)', (room,))
    db.commit()
    display_menu()


def _get_room_name():
    """Get a unique room name from the user."""
    room = input("Enter a name for the room: ")
    if room == "":
        print("Room name is required.")
        _get_room_name()
    room_query = list(db.execute("SELECT name from room").fetchall())
    rooms = [r[0].lower() for r in room_query]
    if room.lower() in rooms:
        print("Room name must be unique. The following room names are taken: ")
        for r in rooms:
            print(r)
        print('\n')
        _get_room_name()
    else:
        return room


def print_inventory():
    """Print the inventory of the room plus the value."""
    pass


if __name__ == "__main__":
    welcome()
