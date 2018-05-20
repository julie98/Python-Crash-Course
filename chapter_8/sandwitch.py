def order_sandwitch(*orders):
	"""sandwitch info"""
	print("\nThe sandwitch contains:")
	for order in orders:
		print("-" + order)

order_sandwitch('strawberry')
order_sandwitch('pastrami', 'pork')
order_sandwitch('pineapple', 'beef', 'cheese')
