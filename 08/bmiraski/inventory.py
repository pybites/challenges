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
    print("UPDATE A ROOM".center(80))
    print("-".center(80, '-'))
    r = _update_which_room()
    item = _add_item()
    value = _get_value(item)
    db.execute('''INSERT into items (item_name, item_value, room_id)
               VALUES (?, ?, ?)''', (item, value, r))
    db.commit()
    print(
        f'''{item.capitalize()} with value of ${value:.2f} has been added to the room.\n'''
         )
    display_menu()


def _update_which_room():
    """Get the room to update."""
    room_query = list(db.execute("SELECT name from room").fetchall())
    rooms = [r[0].lower() for r in room_query]
    print('Room choices: ' + ', '.join(rooms))
    room = input('Which room would you like to update: ').lower()
    while room not in rooms:
        print('That is not a valid room.')
        room = input('Which room would you like to update: ').lower()
    r_id = tuple(db.execute("SELECT id from room where name LIKE ? ", (room, )
                           ).fetchone())[0]
    return r_id


def _add_item():
    """Get the name of the item to add."""
    item = input("What item would you like to add to the room: ").lower()
    while item == "":
        print("Item name is required.")
        item = input("What item would you like to add to the room: ").lower()
    return item


def _get_value(item):
    value = 0
    while value <= 0:
        try:
            value = float(input(f'What is the value of the {item}: '))
            if value < 0:
                print("The value must be positive.")
        except ValueError:
            print("The item's value must be a number.")
    return value


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
    while room == "":
        print("Room name is required.")
        room = input("Enter a name for the room: ")
    room_query = list(db.execute("SELECT name from room").fetchall())
    rooms = [r[0].lower() for r in room_query]
    while room.lower() in rooms:
        print("Room name must be unique. The following room names are taken: ")
        for r in rooms:
            print(r)
        print('\n')
        room = input("Enter a name for the room: ")
    else:
        return room


def print_inventory():
    """Print the inventory of the room plus the value."""
    inventory = db.execute("""SELECT name, i.id, room_id, item_name, item_value
                from items i JOIN room r on i.room_id = r.id
                ORDER BY name ASC""").fetchall()
    inventory = list(inventory)
    print(inventory)
    pass


if __name__ == "__main__":
    welcome()
