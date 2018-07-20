import sys

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

				print(item + ':' + ' ' + element)

			print("======================================")


	def __len__(self):

		return len(self.house_structure)


	def __getitem__(self, key):

	    for k,v in self.house_structure[key].items():
	        print(k,v) 


def main():

	data_dictionary = dict()

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

	#print(house[room_list[0]])

	print(len(house))


	s = ','.join(room_list)

	print(s)

	room = input("Out of above mentioned room, enter room name you wish to list?")

	if room in data_dictionary.keys():
	    house[room]
	else:
		print("Invalid Room")



if __name__ == '__main__':

	
	print("HOUSE INVENTORY TRACKER")

	while True:

		choice = int(input("Press 1: to start listing rooms and items for 1st time\nPress 2: To exit\n"))

		if choice == 1:
			main()
		elif choice == 2:
			break
