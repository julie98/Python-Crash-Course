def describe_city(name, country = 'china'):
	"""display a city and its country"""
	print("\n" + name.title() + " is in " + country.title() + ".")


describe_city(name = 'beijing')
describe_city('new york', 'united states')
describe_city('paris', 'france')
describe_city('london', 'united kingdom')