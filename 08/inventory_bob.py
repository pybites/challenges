from collections import defaultdict, namedtuple

NUM_ITEMS = 5
ROOMS = 'study living_room master_bedroom'.split()

Item = namedtuple('Item', 'name value')
inventory = defaultdict(list)


def get_name():
    while True:
        name = input('- Enter the name of the item: ')
        if not name:
            print('Name cannot be blank')
            continue
        else:
            return name


def get_value():
    while True:
        try:
            value = int(input('- Enter the value of the item: '))
            return value
        except ValueError:
            print('Value needs to be a number, try again')
            continue


def calc_totals(inventory):
    totals = {}
    for room, items in inventory.items():
        totals[room] = sum(it.value for it in items)
    return totals


if __name__ == "__main__":
    for room in ROOMS:
        print('\nEntering items for room {}:\n'.format(room))
        for i in range(NUM_ITEMS):
            print('* Item #{}:'.format(i + 1))
            name = get_name()
            value = get_value()
            item = Item(name, value)
            inventory[room].append(item)

    totals = calc_totals(inventory)

    fmt = '{:<15}: {:>5}'
    for room, items in inventory.items():
        print('\n* Room: {}'.format(room))
        for it in items:
            print(fmt.format(it.name, it.value))
        print('--')
        print(fmt.format('Subtotal', totals[room]))
    print('\n----')
    print(fmt.format('Total', sum(totals.values())))
