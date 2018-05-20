def build_profile(first, last, **user_info):
	"""build  dictionary, which incldue everything we know about users"""
	profile = {}
	profile['first_name'] = first.title()
	profile['last_name'] = last.title()
	for key, value in user_info.items():
		profile[key] = value.title()
	return profile

user_profile = build_profile('haoyu', 'zhu', location = 'stanford', field = 'computer science', hobby = 'piano')
print(user_profile)