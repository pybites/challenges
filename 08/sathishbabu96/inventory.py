import json

ROOMS = {}


def add_room():
    _room = input('Enter Room name: ')
    room = {'name': _room,
            'items': {}}
    while True:
        item_details = input('Enter item details(name, value): ').split(' ')
        name, value = item_details
        room.get('items')[f'{name}'] = int(value)
        choice = input('Wanna add more? y or n: ').lower()
        if choice == 'n' or choice == 'no':
            break
    ROOMS[f'{_room}'] = room


def update_room():
    _room = input(f'Enter Room name(Available rooms are {list(ROOMS.keys())}: ')
    room_items = ROOMS.get(f'{_room}').get('items')
    while True:
        item_details = input('Enter item details(name, value): ').split(' ')
        name, value = item_details
        if name in room_items:
            room_items[f'{name}'] = int(value)
        choice = input('Wanna add more? y or n: ').lower()
        if choice == 'n' or choice == 'no':
            break


def list_room():
    _room = input(f'Enter Room name(Available rooms are {list(ROOMS.keys())}: ')
    room = ROOMS.get(_room)
    room_value = 0
    print('##'*30)
    print(f'Room: {room.get("name")}')
    for item, value in room.get('items').items():
        print(f'Item:\n\tName: {item}\n\tValue: {value}')
        room_value += value
    print(f'Room value: {room_value}')


def get_cost(room=None):
    if room is None:
        _room = input(f'Enter Room name(Available rooms are {list(ROOMS.keys())}: ')
    else:
        _room = room
    print('##' * 30)
    if _room == 'all':
        for room in ROOMS:
            get_cost(room)
        print(f'Total house value: {sum([sum(ROOMS.get(room).get("items").values()) for room in ROOMS])}')
    else:
        print(f'{_room} room value: {sum(ROOMS.get(_room).get("items").values())}')


def start():
    global ROOMS
    with open('rooms.json', 'r') as fp:
        data = fp.read()
    if data:
        ROOMS = json.loads(data)
    while True:
        print('##' * 30)
        choice = int(input('''Please enter your choice:
    1. Add Room
    2. List Room
    3. Update Room
    4. Show total value
    5. End
            '''))
        if choice == 1:
            add_room()
        elif choice == 2:
            list_room()
        elif choice == 3:
            update_room()
        elif choice == 4:
            get_cost()
        elif choice == 5:
            with open('rooms.json', 'w') as fp:
                json.dump(ROOMS, fp)
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    start()
