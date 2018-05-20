pets = []

pet = {
	'name' : 'George',
	'type' : 'poodle',
	'owner' : 'Julie',
}
pets.append(pet)

pet = {
	'name' : 'Duoduo',
	'type' : 'poodle',
	'owner' : 'Ziyan',
}
pets.append(pet)

pet = {
	'name' : 'Zaizai',
	'type' : 'poodle',
	'owner' : 'Zaiba',
}
pets.append(pet)


for pet in pets:
	print(pet['name'].title() + " is a " + pet['type'] + ", whose owner is " + pet['owner'] + ".")