class Dog():
	"""a simple tempt to simulate a dog"""

	def __init__(self, name, age):
		self.name = name.title()
		self.age = age

	def sit(self):
		print(self.name + " is now sitting.")

	def roll_over(self):
		print(self.name + " rolled over!")


my_dog = Dog("George", 1)
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) +" year-old!")

my_dog.sit()
my_dog.roll_over()