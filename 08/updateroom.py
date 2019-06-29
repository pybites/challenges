def update(room):
    name = input("Which room would you like to change?: ")
    action = input("Do you wish to:\n1: Add a new item\n2: Delete an item\nEnter a number: ")
    item = input("Name of item?: ")
    if action == "1":
        price = input("Price of item?: ")
        room[name].extend([item, price])
    elif action == "2":
        del room[name][room[name].index(item)+1]
        del room[name][room[name].index(item)]
    else:
        print("Please enter valid option")
        update(room)
    return room