import json

file_obj = open("data.json")
data_dict = json.load(file_obj)
file_obj.close()

def room_specific_info():
    room_count = len(data_dict)
    if room_count <= 0:
        print("There are no expense info for any rooms. Please input data in DB.\nTerminating the program...")
        exit()
    
    print(f"You have totally {room_count} rooms. Please select one from the below")
    room_list = data_dict.keys()
    for index, each_room in enumerate(room_list):
        print(f"{index+1}. {each_room}")
    
    selected_room = input()
    if selected_room.capitalize() not in room_list:
        print("You have inputted an invalid room ID. Terminating the program...")
        exit()
    
    print(f"\n{selected_room.capitalize()} has totaly {len(data_dict[selected_room.capitalize()])} items")
    items_dict = data_dict[selected_room.capitalize()]
    for item, value in items_dict.items():
        print(f"{item} -----> Rs.{value} ")

    continue_to_home = input("\nDo you want to go to Home page[Y/N]")
    if continue_to_home.lower() == 'y':
        home_page()
    else:
        print("GoodBye, have a nice day...")
        exit()


def overall_expense_overview():
    room_count = len(data_dict)
    print(f"You have totally {room_count} rooms")
    for room_name,items_dict in data_dict.items():
        items_count = len(items_dict)
        net_val = 0
        for item_name, item_value in items_dict.items():
            net_val = net_val + item_value
        print(f"Your {room_name} has {items_count} items with net value of {net_val}")
    
    continue_to_home = input("\nDo you want to go to Home page[Y/N]")
    if continue_to_home.lower() == 'y':
        home_page()
    else:
        print("GoodBye, have a nice day...")
        exit()


def add_inventory_to_db():
    room_name = input("Enter the Room name : ").capitalize().strip()
    inventory_item = input("Enter the inventory item : ").capitalize().strip()
    try:
        item_price = input("Enter the inventory price : ")
        item_price = int(item_price)
    except Exception as e:
        print("There is an exception while inputting the inventory price : " + e)
        print("Terminating the program")
        exit()

    if room_name in data_dict.keys():
        inventory_dict = data_dict[room_name]
        if inventory_item not in inventory_dict.keys():
            data_dict[room_name].update({inventory_item : item_price})
        else:
            print(f"This inventory is already present in this room and has the price {inventory_dict[inventory_item]}")
            update_inventory_value = input("Do you want to update the value of this inventory?[Y/N]")
            if update_inventory_value.lower() == 'y':
                data_dict[room_name].update({inventory_item : item_price})
            else:
                print("keeping the item value as it is... Redirecting to home page..")
                home_page()
                return 0
    else:
        inventory_dict = {inventory_item : int(item_price)}
        room_dict = {room_name : inventory_dict}
        data_dict.update(room_dict)
    
    json_file_obj = open("data.json", 'w')
    json.dump(data_dict, json_file_obj)
    json_file_obj.close()
    
    
def home_page():
    user_options = '''Please select one of the following options\n\
    A ->  Display overview of the expense\n\
    B ->  Display Roomwise detailed Info\n\
    C ->  Add new inventory to the database \n\
    D ->  To terminate the conversation\n\
    '''
        
    print(user_options)
    selected_option = input()
    if selected_option.lower() == 'a':
        overall_expense_overview()
    elif selected_option.lower() == 'b':
        room_specific_info()
    elif selected_option.lower() == 'c':
        add_inventory_to_db()
    elif selected_option.lower() == 'd':
        print("GoodBye, have a nice day...")
        exit()
    else:
        print("Invalid input. Terminating the program.....")


def main():
    print("Hi, Welcome to your expense info...")
    home_page()

    
main()