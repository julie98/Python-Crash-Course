favorite_places = {
	'Julie' : ['Xiamen', 'New York'],
	'Karolina' : ['Los Angeles', 'Long Island'],
	'George' : ['America', 'Japan', 'Cannada'],
	'Angela' : ['Atlanta'],
}


for name, cities in favorite_places.items():
	if len(cities) > 1:
		print("\n" + name.title() + "'s favorite cities are:")
		for city in cities:
			print("\t" + city.title())
	else:
		print("\n" + name.title() + "'s favorite city is:")
		print("\t" + city.title())
