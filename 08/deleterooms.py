def delete(rooms):
    name = input("Enter name of room: ")
    del rooms[name]
    return rooms