file_name = 'inquiry_results.txt'

print("Please enter 'quit' when you're finished.")
while True:
	reason = input("Why are you fond of programming? ")
	if reason == 'quit':
		break;
	else:
		with open(file_name, 'a') as file_object:
			file_object.write(reason + "\n")