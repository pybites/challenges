# inventory.py - House Inventory Tracker
# https://pybit.es/articles/codechallenge08/


ROOMS = {
    'kitchen': [
        {'name': 'stove', 'price': 500.00},
        {'name': 'table', 'price': 100.00},
        {'name': 'chairs', 'price': 50.00},
        {'name': 'cupboard', 'price': 75.00},
        {'name': 'pots & pans', 'price': 250.00},
    ],
    'living room': [
        {'name': 'couch', 'price': 50.00},
        {'name': 'recliner', 'price': 100.00},
        {'name': 'TV', 'price': 150.00},
        {'name': 'cupboard', 'price': 75.00},
        {'name': 'ottoman', 'price': 25.00},
    ],
    'bedroom': [
        {'name': 'bed', 'price': 250.00},
        {'name': 'bedding', 'price': 100.00},
        {'name': 'nightstand', 'price': 150.00},
        {'name': 'cupboard', 'price': 75.00},
        {'name': 'clothes', 'price': 25.00},
    ],
}


if __name__ == "__main__":
    grand_total = 0
    for room, items in ROOMS.items():
        room_total = 0
        print(room.upper())
        # print('-' * len(room))
        for item in items:
            print(f'{item["name"].title():<15}: {item["price"]:7.2f}')
            room_total += item['price']
        print('-' * 24)
        print(f'{room_total:24.2f}')
        grand_total += room_total
    print('=' * 24)
    print(f'{grand_total:24.2f}')

