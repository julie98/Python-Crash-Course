class Restaurant():
	""" """
	def __init__(self, restaurant_name, cuisine_type):
		""" """
		self.name = restaurant_name.title()
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		msg = self.name + " serves wonderful " + self.type + "."
		print("\n" + msg)

	def open_restaurant(self):
		msg = self.name + "is open!"
		print("\n" + msg)

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment):
		self.number_served += increment

# mean_queen = Restaurant('the mean queen', 'pizza')
# mean_queen.describe_restaurant()

# ludvigs = Restaurant("ludvig's bistro", 'seafood')
# ludvigs.describe_restaurant()

# mango_thai = Restaurant('mango thai', 'thai food')
# mango_thai.describe_restaurant()

# restaurant = Restaurant('pizza hut', 'pizza')
# print(restaurant.name + " has served " +str(restaurant.number_served) + " people.")

# restaurant.number_served = 50
# print("\nNumber served: " + str(restaurant.number_served))

# restaurant.increment_number_served(100)
# print("\nNunber_served: " + str(restaurant.number_served))

