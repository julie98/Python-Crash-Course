favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

coders = ['jen', 'sarah', 'edward', 'phil', 'julie', 'eric', 'karolina']

# print("Phil's favorite language is " + favorite_languages['phil'].title() + ".")


# for name, language in favorite_languages.items():
# 	print(name.title() + "'s favorite language is " + language.title() + ".")

# for name in favorite_languages.keys():
# 	print(name.title())

# for name in sorted(favorite_languages.keys(), reverse = True):
# 	print(name.title())

# for language in set(favorite_languages.values()):
# 	print(language.title())

for coder in coders:

	if coder in favorite_languages.keys():
		print(coder.title() + ", thanks for taking our poll!")
	else:
		print(coder.title() + ", what's your favorite language?")
