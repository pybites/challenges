def view(rooms, name):
    print(name+": ")
    
    objects = [item for item in rooms[name][::2]]
    prices = [item for item in rooms[name][1::2]]

    for i, j in zip(objects, prices):
        print("The item {} cost £{}".format(i, j))