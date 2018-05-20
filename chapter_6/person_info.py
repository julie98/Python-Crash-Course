person_0 = {
	'first_name' : 'Haoyu',
	'last_name' : 'Zhu',
	'age' : 20,
	'city' : 'Tianjin',
}

person_1 = {
	'first_name' : 'Zifan',
	'last_name' : 'Tian',
	'age' : 22,
	'city' : 'Shijiazhuang',
}

person_2 = {
	'first_name' : 'George',
	'last_name' : 'Zhu',
	'age' : 1,
	'city' : 'Linyi',
}

# print(person_0['first_name'])
# print(person_0['last_name'])
# print(person_0['age'])
# print(person_0['city'])

people = [person_0, person_1, person_2]

for person in people:
	full_name = person['first_name'].title() + " " + person['last_name'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(full_name + ", who live in " + city + ", is " + age + "-year-old.")
