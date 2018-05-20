prompt = "\nWhat topping would you like on your pizza? "
prompt += "\nEnter 'quit' when you're finished. "

active = True
while active:
	topping = input(prompt)
	if topping != 'quit':
		print("I'll add " + topping + " on my pizza.") 
	else:
		active = False
