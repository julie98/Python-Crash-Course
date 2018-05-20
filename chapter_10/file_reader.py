# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents)

# pi_string = ''
# for line in contents:
# 	pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))

# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
# 	for line in file_object:
# 		print(line)

file_path = '/Users/zhy/python_work/test.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# 	print(contents)


# with open(file_path) as file_object:
# 	for line in file_object:
# 		print(line.rstrip())

# file_path = 'pi_digits.txt'
with open(file_path) as file_object:
	lines = file_object.readlines()

# for line in lines:
# 	print(line)

pi_string = ''
for line in lines:
	pi_string += line

# print(pi_string)
# print(len(pi_string))


# file_path = '/Users/zhy/Downloads/《Python编程》源代码文件/chapter_10/pi_million_digits.txt'
# with open(file_path) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# birthday = input("Please enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
# 	print("Your birthday appears in the first million digits of pi!")
# else:
# 	print("Your birthday does not appear in the first million digits of pi.")

# print(pi_string[:52] + "...")
# print(len(pi_string))

print(pi_string)

print(pi_string.replace('a', 'A'))