my_pizzas = ['chicken', 'pineapple', 'beaf', 'duck']
friend_pizzas = my_pizzas[:]
# for pizza in my_pizzas:
# 	message = "I like " + pizza + " pizza!\n"
# 	print(message)
# print("I really love pizza!")

friend_pizzas.append('pepperoni')
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
	print(my_pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
