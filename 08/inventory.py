from pony.orm import *

db = Database()

class Room(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    items = Required(Json)

db.bind('sqlite', ':memory:', create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def create_inventory():
    Living = Room(name = 'Living Room',
              items = {
                'TV':300,
                'Couch':500,
                'sideboard':400
              })

    Dining = Room(name = 'Dining Room',
              items = {
                'Table': 500,
                'Fish Tank': 100,
                'Painting': 500
              })

    Kitchen = Room(name = 'Kitchen',
                   items = {
                       'Fridge': 500,
                       'Stove': 300,
                       'Mixer': 300
                   })

    Bedroom = Room(name = 'Bedroom',
                   items = {
                       'bed': 1000,
                       'desk': 100,
                       'shelves': 100
                   })

create_inventory()

inventory  = {'living room': {'TV':300, 'Couch':500,'sideboard':400},
              'dining roon': {'Table': 500, 'Fish Tank': 100, 'Painting': 500},
              'kitchen': {'Fridge': 500, 'Stove': 300, 'Mixer': 300},
              'Bedroom': {'bed': 1000, 'desk': 100, 'shelves': 100}}

for room, items in inventory.items():
    print(f'In the {room} there are the following items: ')
    for item, value in items.items():
        print(f'    A {item} worth ${value}')
