sandwitch_orders = ['tuna', 'pastrami', 'pineapple', 'pastrami', 'pork', 'turkey', 'pastrami']
finished_sandwitches = []


print("\nI'm sorry, we're out of pastrami today.")
while 'pastrami' in sandwitch_orders:
	sandwitch_orders.remove('pastrami')


print('\n')
while sandwitch_orders:
	current_sandwitch = sandwitch_orders.pop()
	print("I'm working on your " + current_sandwitch + " sandwitch.")
	finished_sandwitches.append(current_sandwitch)

print("\n")
for sandwitch in finished_sandwitches:
	print("I made a " + sandwitch + " sandwitch.")