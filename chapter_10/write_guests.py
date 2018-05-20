file_name = 'guest.txt'


name = input("What's your name? ")
with open(file_name, 'a') as file_object:
	file_object.write("name")