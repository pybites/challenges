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
        print(', '.join(rooms))
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
    choice = 0
    while choice not in range(1, 3):
        try:
            choice = int(input(
                'Would you like to (1) print one room, (2) print all rooms: '
                ))
        except ValueError:
            print("Please make a valid choice")
    if choice == 1:
        room = _get_inv_room()
        print_room_inv(room)
    else:
        inv_values = db.execute("SELECT item_value from items").fetchall()
        inv_values = list(inv_values)
        total = sum(val[0] for val in inv_values)
        rooms = list(db.execute("SELECT id FROM room").fetchall())
        rooms = [room[0] for room in rooms]
        for room in rooms:
            print_room_inv(room)
        print("=".center(50, "="))
        print('Grand Total:' + '{0:>28}{1:>10.2f}\n'.format('$', total))
    display_menu()


def _get_inv_room():
    """Get the room for inventory."""
    room_query = list(db.execute("SELECT name from room").fetchall())
    rooms = [r[0].lower() for r in room_query]
    print('Room choices: ' + ', '.join(rooms))
    room = input(
        'Which room would you like to print the inventory for: '
        ).lower()
    while room not in rooms:
        print('That is not a valid room.')
        room = input('Which room would you like to update: ').lower()
    r_id = tuple(db.execute("SELECT id from room where name LIKE ? ", (room, )
                           ).fetchone())[0]
    return r_id


def print_room_inv(room):
    """Print a single room's inventory."""
    room_name = tuple(db.execute("SELECT name from room where id = ?", (room, )
                                ).fetchone())[0]
    print(f"\nRoom inventory for {room_name}")
    print("-".center(50, "-"))
    room_inv = db.execute("""SELECT item_name, item_value from items
                             WHERE room_id = ?""", (room,)).fetchall()
    if len(list(room_inv)) == 0:
        print("Room is empty.\n")
        return
    else:
        room_inv = list(room_inv)
        w = max(len(item[0]) for item in room_inv)
        room_total = sum(item[1] for item in room_inv)
        for item in room_inv:
            print('.....{0:<{width}}{1:>5}{2:>10.2f}'
                  .format(item[0], '$', item[1], width=30))
        print("-".center(50, '-'))
        print('Total' + '{0:>35}{1:>10.2f}\n'.format('$', room_total))
    return


if __name__ == "__main__":
    welcome()
