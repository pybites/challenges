import csv
import os


def main():
    """
    Function to ask user whether to print room items from csv file or enter room items and print it.
    """
    answer = int(input("*Press 1 to print the items in room, \n*Press 2 to enter items in all the rooms. "))
    if answer == 1:
        print_room_items_from_csv()
    elif answer == 2:
        room_items = input_room_items()
        write_to_csv_file(room_items)
        print_room_items_from_csv()
    else:
        main()


def print_room_items_from_csv():
    """
    Function to read room items from csv file and print it
    """
    file = os.path.join(os.path.dirname(__file__), "room_items.csv")
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("{:<20}\t{:<40}\t{}".format(row[0], row[1], row[2]))


def input_room_items():
    """
    Function to ask user about the items in the rooms and their price
    :return: a dictionary that contains room names, items and their price
    """
    num_of_rooms = int(input("How many rooms do you have? "))
    room = dict()
    for i in range(1, num_of_rooms + 1):
        room_items = []
        room_name = str(input("Name the room {}: ".format(i)))
        num_items = int(input("How many items do you have in {}? Should be at least 5. ".format(room_name)))
        while num_items < 5:
            num_items = int(input("How many items do you have in {}? Should be at least 5. ".format(room_name)))

        for item in range(1, num_items + 1):
            item_name = input("Enter item {} in {}: ".format(item, room_name))
            value = input("Enter the value of {} in {}: ".format(item_name, room_name))
            room_item = {
                "item": item_name,
                "value": value
            }
            room_items.append(room_item)

        room[room_name] = room_items
    return room


def write_to_csv_file(room_items):
    """
    Function to write room details in csv file
    :param room_items: dictionary containing room details
    """
    file = os.path.join(os.path.dirname(__file__), "room_items.csv")
    with open(file, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Rooms", "Items", "Price($)"])
        for room, items in room_items.items():
            for item in items:
                writer.writerow([room, item["item"], item["value"]])


if __name__ == "__main__":
    main()
