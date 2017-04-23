import pymongo
client = pymongo.MongoClient()
db = client.inventory
house = db.house

def create_inventory(collection):
    Rooms=[{'name' : 'Living Room',
             'items' : {
                'TV':300,
                'Couch':500,
                'sideboard':400
            }},
            {'name' : 'Dining Room',
             'items' : {
                'Table': 500,
                'Fish Tank': 100,
                'Painting': 500
            }},
            {'name' : 'Kitchen',
             'items' : {
                'Fridge': 500,
                'Stove': 300,
                'Mixer': 300
            }},
            {'name' : 'Bedroom',
             'items' : {
                'bed': 1000,
                'desk': 100,
                'shelves': 100
            }}
    ]
    collection.insert_many(Rooms)

def create_room(name, items, collection=house):
    """Create a new room that doesnt already exist"""
    room = {'name': name, 'items': items}
    collection.insert_one(room)


def update_item(room_name, item_name, item_value, collection=house):
    """Update the value of an item in a room  """
    collection.update({"name":room_name}, {'$set': {f'items.{item_name}': item_value}})



if house.count() == 0:
    create_inventory(house)

def show_inventory():
    inv = ''
    for room in house.find():
        inv += f'<p>In the {room["name"]} there are the following items:</p>'
        for item, value in room["items"].items():
            inv += f'<p>A {item} worth ${value}</p>'

    return inv
