class HouseInventory(object):

	def __init__(self, room_list=[]):

		self.room_list = room_list


	def create_rooms(self):

		global data_dictionary

		for room in self.room_list:

			item_list = str(input("Enter list of item names present in {}".format(room))).split(",")

			item_dictionary = dict()

			for item in item_list:

				item_cost = str(input("For {} present in {} enter the item cost".format(item, room)))

				item_dictionary[item] = item_cost

				data_dictionary[room] = item_dictionary

			print("=============================================================================")


	def update_information(self):

		global data_dictionary

		for room in self.room_list:

			for k, v in data_dictionary[room].items():
					
				print(k + ':' + ' ' + v)

			input_item = input("Enter item you wish to Update or add new item?").split(",")

			for item in input_item:

				input_cost = input("Enter cost for {}".format(input_item))

				data_dictionary[room][item] = input_cost


	def delete_room(self):

		global data_dictionary

		room = input("Enter Room name to be deleted?")

		if room in data_dictionary.keys():

			del data_dictionary[room]



	def get_format_output(self):
		"""
		Format the output.
		Based on contents in 
		dictionary
		"""
		for room, item_list in data_dictionary.items():

			print("Room: {}".format(room))

			for item, element in item_list.items():

				print(item + ':' + ' ' + element)

			print("======================================")


	def __len__(self):

		return len(self.house_structure)


	def __getitem__(self, key):

	    for k,v in data_dictionary[key].items():
	        print(k,v)


class HouseInventoryCost:


	def get_room_cost(self, room, **kwargs):

		room_cost = 0

		if room in kwargs.items():
			for value in kwargs[room].items():
				room_cost += int(value)
		return room_cost


	def get_house_cost(self, **kwargs):

		total_cost = 0

		for key, value in kwargs.items():
			for cost in value.values():
				total_cost += int(cost)

		return total_cost


if __name__ == '__main__':

	data_dictionary = dict()
	
	print("HOUSE INVENTORY TRACKER")

	
	while True:

		choice = int(input("Press 1: Create Rooms\nPress 2: Update information\nPress 3: Delete Rooms\nPress 4:Enter room name you wish to list?\nPress 5: List total number of rooms\nPress 6: Cost of House\nPress 7:Cost of One Room\nPress 8: Exit\n"))

		if choice != 8 and choice!=6:

			room_list = str(input("Enter Room Name")).split(",")
			house = HouseInventory(room_list)

		if choice == 1: 

			house.create_rooms()

		elif choice == 2:

			house.update_information()

		elif choice == 3:

			print("For your reference following are the list of rooms, items:  ")
			
			house.get_format_output()

			house.delete_room()
			
		elif choice == 4:

			s = ','.join(room_list)
			print(s)

			for room in room_list:
				if room in data_dictionary.keys():
					house[room]
				else:
					print("Invalid Room")

		elif choice == 5:
			print("Total number of rooms in house are {}".format(len(house)))

		elif choice == 7:

			housecost = HouseInventoryCost()
			if len(room_list) == 1:
				room = ''.join(room_list)
				print("Cost for room {} is".format(room))
				print(housecost.get_room_cost(room, **data_dictionary))
				print("Computes cost for only 1 room wrong input")

		elif choice == 6:

			housecost = HouseInventoryCost()
			print("Total House Cost is  ")
			print(housecost.get_house_cost(**data_dictionary))

		elif choice == 8:
			break

		house.get_format_output()