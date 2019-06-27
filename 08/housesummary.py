from viewroom import view

def summary(rooms):
    for room in rooms.keys():
        view(rooms, room)