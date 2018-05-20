def show_magicians(magicians):
	"""show magicians' name using a list"""
	for magician in magicians:
		print(magician.title() + " ")

def make_great(magicians):
	"""make magicians great"""

	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magician = "the Great " + magician
		great_magicians.append(great_magician)

	for great_magician in great_magicians:
		magicians.append(great_magician)

	return magicians

	

magicians = ['harry houdini', 'david blaine', 'teller']


print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)