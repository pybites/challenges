class Room:
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.value = 0

    def add_item(self):
        item = input('Item name: ').title()
        price = int(input('Price of item: '))

        self.items[item] = price
        self.value += price
        print(f'{item} was added to {self.name}.\n')

    def remove_item(self):
        item = input('Which item would you like to remove? ').title()

        try:
            del self.items[item]
            print(f'{item} was deleted.')
        except KeyError:
            print(f'Could not remove {item} because it does not exist.\n')

    def update_price(self):
        item = input("Which item's price would you like to update? ").title()
        for item in self.items:
            print(item)

        price = int(input('What is the new price? '))

        self.items.update({item: price})
        print(f"{item}'s price has been updated to ${price}.\n")


rooms = []


def main():
    print('Welcome to the Home Inventory Tracker!')

    while True:
        print('What would you like to do?')
        # The following multi line string looks weird.
        # I assume there must be a better way to do this.
        print("""
1. Create a room
2. Update a room
3. Show total dollar value
4. Show rooms
5. Quit\n""")

        choice = input().lower()
        possible_choices = {
            'create a room': create_room,
            'update a room': update_room,
            'show total dollar value': print_total_value,
            'show rooms': print_rooms,
        }

        try:
            possible_choices[choice]()
        except KeyError:
            if choice == 'quit':
                print('Goodbye!')
                break

            print('That is not a valid option. Try again.')
            continue


def create_room():
    """Allows a user to create a room with items."""
    name = input("What is the name of the room?\n").title()
    number_of_items = int(input('How many items would you like to list? (Must be a minimum of 5) '))

    if number_of_items < 5:
        print('Number of items must be at least 5.')
        return

    room = Room(name=name)

    for _ in range(number_of_items):
        room.add_item()

    rooms.append(room)


def update_room():
    """Allows the user to update a certain part of a room."""
    print('Which room would you like to update?\n')
    for room in rooms:
        print(room.name)

    room_to_update = input().title()
    chosen_room = None

    for i, room in enumerate(rooms):
        if room.name == room_to_update:
            chosen_room = i

    try:
        room = rooms[chosen_room]
    except KeyError:
        print('That room does not exist.')
        return

    print("What would you like to update?\n")
    print("""1. Add item
2. Remove item
3. Update price
4. Main menu""")

    choice = input().lower()
    possible_choices = {
        'add item': room.add_item,
        'remove item': room.remove_item,
        'update price': room.update_price,
    }

    try:
        possible_choices[choice]()
    except KeyError:
        if choice == 'main menu':
            return

        print('That is not a valid option.')


def print_total_value() -> int:
    """Prints the total value of the house (value of all rooms combined)"""
    print(f'Total value of house: ${sum([room.value for room in rooms])}')


def print_rooms():
    """Prints out each room with the list of items and prices."""
    if not rooms:
        print('No rooms to list. You have to add a room first.')
        return

    for room in rooms:
        print()
        print(f'{room.name}:\n')
        for item, price in room.items.items():
            print(f'- {item:<5}: ${price}')

        print()


if __name__ == "__main__":
    main()
