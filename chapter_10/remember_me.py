import json

user_name = input("What is your name? ")

file_name = 'username.json'
with open(file_name, 'w') as f_obj:
	json.dump(user_name, f_obj)
	print("We'll remember you when you come back, " + user_name + "!")