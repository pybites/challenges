study = {"computer": 1200, "lg flatron monitor": 300, "samsung monitor": 500, "desk": 400, "guitar": 500}
living_room = {"couch": 1000, "tv": 3000, "playstation": 500, "speakers": 600, "beanbag": 30}
master_bedroom = {"bed": 400, "mattress": 1000, "chair": 180, "drawers": 250, "lamp": 20}

rooms = {"Study": study, "Living Room": living_room, "Master Bedroom": master_bedroom}

def print_contents(room):
   for k, v in room.items():
       print('\n' + k)
       for key, val in v.items():
           print("{}: ${}".format(key, val))


def sum_of_rooms(room):
   print('\nTotals:')
   for k, v in room.items():
       print("{}: ${}".format(k, (sum(v.values()))))


print_contents(rooms)
sum_of_rooms(rooms)
