current_users = ['admin', 'Julie', 'Angela', 'Eric', 'Karolina']

new_users = ['Gisele', 'Angela', 'Eugenia', 'Kate', 'John', 'eric']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("This name has been taken!")
	else:
		print("This name is still available!")
