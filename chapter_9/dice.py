from random import randint

class Die():
	def __init__(self,sides = 6):
		self.sides = sides

	def roll_die(self):
		return randint(1, self.sides)

results = []
die_one = Die(10)
for roll_number in range(10):
	result = die_one.roll_die()
	results.append(result)
print(results)

results = []
die_two = Die(20)
for roll_number in range(20):
	result = die_two.roll_die()
	results.append(result)
print(results)