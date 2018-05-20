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

class IceCreamstand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def show_flavors(self):
		for flavor in self.flavors:
			print(flavor + " ")

ice_cream = IceCreamstand('Dairy Queen')
ice_cream.flavors = ['vanilla', 'pineapple', 'strawberry', 'grape']
ice_cream.show_flavors()