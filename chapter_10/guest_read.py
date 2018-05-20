file_name = 'inquiry_results.txt'

with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)