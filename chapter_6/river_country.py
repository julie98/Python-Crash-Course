rivers = {
	'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
	print("\nThe " + river.title() + " runs though " + country + ".")

for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())