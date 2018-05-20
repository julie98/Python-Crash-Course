def make_car(manufac, mdl, **car_info):
	"""car info"""
	profile = {}
	profile['manufacturer'] = manufac
	profile['model'] = mdl
	for key, value in car_info.items():
		profile[key] = value
	return profile
