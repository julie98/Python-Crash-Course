favortite_numbers = {
	'Julie' : [3, 16],
	'Eric' : [6, 12],
	'George' : [8, 88],
	'Karolina' : [5, 15],
	'Angela' : [7, 17],
}

# num = favortite_numbers['Julie']
# print("Julie's favorite number is " + str(num) + ".")

# num = favortite_numbers['Eric']
# print("Eric's favorite number is " + str(num) + ".")

# num = favortite_numbers['George']
# print("George's favorite number is " + str(num) + ".")

# num = favortite_numbers['Karolina']
# print("Karolina's favorite number is" + str(num) + ".")

# num = favortite_numbers['Angela']
# print("Angela's favorite number is" + str(num) + ".")

for name, nums in favortite_numbers.items():
	print("\n" + name + "'s favorite numbers are :")
	for num in nums:
		print("\t" + str(num))