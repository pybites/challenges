from createrooms import create
from updateroom import update
from deleterooms import delete
from viewroom import view
from housesummary import summary

def main():
    with open("rooms.txt","r") as f:
        rooms = {}
        for line in f:
            contents = line.strip().split(" : ")
            sub_contents = contents[1].split(", ")
            rooms[contents[0]] = sub_contents
    
    print("Which action would you like to take? The options are: \n1: Create room\n2: Update room\n3: Remove room\n4: View room\n5: View summary")
    action = input("Please input a number: ")

    if action == "1":
        rooms = create(rooms)
    elif action == "2":
        rooms = update(rooms)
    elif action == "3":
        rooms = delete(rooms)
    elif action == "4":
        name = input("Enter room name: ")
        view(rooms, name)
    elif action == "5":
        summary(rooms)
    else:
        print("Please enter an appropriate option")
        main()

    with open("rooms.txt", "w") as f:
        for room in rooms.keys():
            items = ", ".join(rooms[room])
            f.write("{} : {}".format(room, items))
            f.write("\n")

    cont = input("Would you like to continue? y/n: ")
    if cont == "y":
        main()

main()