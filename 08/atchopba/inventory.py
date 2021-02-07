#!/usr/bin/env python
# encoding: utf-8

from random import randint

ROOM_NAMES = ["bathroom", "leaving room", "study room", "storeroom", "kitchen"]
ITEMS = ["couch", "sofa", "tv", "bidet", "stylo", "pillow", "chair", "table", "microwave", "closet", "painting", "money", "lamp", "laptop", "boots", "chalk"]
PRICES = [500, 1500, 2000, 2400, 2500, 5000, 6000]

class Rooms():
    
    def __init__(self):
        self.room_names = ROOM_NAMES
        
    def _build_items(self, nb_rooms):
        rooms = []
        for k in range(0, nb_rooms):
            room_name_index = randint(0, len(ROOM_NAMES)-1)
            room_name = self.room_names[room_name_index]
            self.room_names.pop(room_name_index)
            items_tmp = ITEMS
            room_items = []
            try:
                room_price = 0
                for i in range(0, 5):
                    item_tmp_index = randint(0, len(items_tmp)-1)
                    item_tmp = items_tmp[item_tmp_index]
                    item_price_tmp = PRICES[randint(0, len(PRICES)-1)]
                    room_price += item_price_tmp
                    room_items.append({"name": item_tmp, "price": item_price_tmp})
                    items_tmp.pop(item_tmp_index)
                rooms.append({"name": room_name, "price": room_price, "items": room_items})
            except ValueError:
                print("Error: not enough elements to compose another room")
        return rooms
        
    def _print(self, nb_rooms):
        rooms_price_total = 0
        rooms = self._build_items(nb_rooms)
        for room in rooms:
            print("\n" + room["name"] + ": "+ str(room["price"]) +"€")
            for item in room["items"]:
                rooms_price_total += item["price"]
                print(item["name"] + " : " + str(item["price"]) + "€")

if __name__ == '__main__':
    Rooms()._print(3)