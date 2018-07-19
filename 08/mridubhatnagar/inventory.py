class HouseInventory(object):

	def __init__(self, house_structure):

		self.house_structure = house_structure
        
        
	def get_format_output(self):
		"""
		Format the output.
		Based on contents in 
		dictionary
		"""
		for room, item_list in self.house_structure.items():

			for item, element in item_list.items():

				print(element + ':' + ' ' + item)

			print("======================================")


	def __len__(self):

		return len(self.house_structure)


	def __getitem__(self, key):

	    return self.house_structure[key] 


if __name__ == '__main__':

	data_dictionary = dict()

	print("HOUSE INVENTORY TRACKER")

	room_list = str(input("Enter room names seprated by comma")).split(",")


	for room in room_list:

		item_dictionary = dict()

		item_list = str(input("Enter list of item name present in {}".format(room))).split(",")

		for item in item_list:

			item_cost = str(input("For item name {} present in room {} enter the item cost".format(item, room)))

			item_dictionary[item] = item_cost

		data_dictionary[room] = item_dictionary

		print("=============================================================================")

	house = HouseInventory(data_dictionary)

	house.get_format_output()

	print(house[room_list[0]])

	print(len(house))

