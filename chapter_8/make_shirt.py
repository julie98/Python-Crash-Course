def make_shirt(size = 'L', message = 'I love Python'):
	"""T-shirt's size and character"""
	print("\nThe T-shirt's size is " + size.upper() + ".")
	print("It has " + "'" + message.upper() + "'" + " on it.")

# make_shirt('s', 'believer')
# make_shirt('m', 'persistence')
# make_shirt('l', 'dream your dream')


make_shirt()
make_shirt(size = 'm')
make_shirt('s', "Hold onto it, and you'll succeed!")