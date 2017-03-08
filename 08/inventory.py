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

if house.count() == 0:
    create_inventory(house)


for room in house.find():
    print(f'In the {room["name"]} there are the following items: ')
    for item, value in room["items"].items():
        print(f'    A {item} worth ${value}')
