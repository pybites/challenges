import sys
print(sys.version)

inventory  = {'living room': {'TV':300, 'Couch':500,'sideboard':400},
              'dining roon': {'Table': 500, 'Fish Tank': 100, 'Painting': 500},
              'kitchen': {'Fridge': 500, 'Stove': 300, 'Mixer': 300},
              'Bedroom': {'bed': 1000, 'desk': 100, 'shelves': 100}}

for room, items in inventory.items():
    print(f'In the {room} there are the following items: ')
    for item, value in items.items():
        print(f'    A {item} worth ${value}')
