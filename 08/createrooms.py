def create(room_dict):
    name = input("What is the name of this room?: ")
    contents = []

    for i in range(1,6):
        item = input("What is the name of the {}th item?: ".format(i))
        price = input("What is the price of the {}?: ".format(item))
        contents.extend([item, price])
    
    room_dict[name] = contents

    return room_dict
    
