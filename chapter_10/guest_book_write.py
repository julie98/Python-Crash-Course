file_name = 'guest_book.txt'

print("Please enter 'quit' when you are finished.")
while True:
	name = input("\nWhat's your name? ")
	if name == 'quit':
		break;
	else:
		with open(file_name, 'a') as file_object:
			file_object.write(name + "\n")
