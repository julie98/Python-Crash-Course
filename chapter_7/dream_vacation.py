responses = {}

name_prompt = "what's your name? "
place_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "Would you like to let another person respond?(Y/N) "

while True:
	name = input(name_prompt)
	place = input(place_prompt)

	responses[name] = place

	repeat = input(continue_prompt)
	if repeat != 'Y':
		break

print("\n--- Poll Results ---")
for name, place in responses.items():
	print(name.title() + "'s favorite place is " + place.title() + ".")
