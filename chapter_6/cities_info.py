cities = {
	'Beijing' : {
	'country' : 'China',
	'population' : 10000000,
	'nearby mountains': 'xishan',
	},
	'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
    }
}

for city, city_info in cities.items():
	country = city_info['country'].title()
	population = str(city_info['population'])
	mountains = city_info['nearby mountains'].title()

	print("\n" + city.title() + " is in " + country + ".")
	print("It has " + population + " people.")
	print("The " + mountains + " mountains are nearby.")
