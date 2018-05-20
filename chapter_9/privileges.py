# class User():
#     """Represent a simple user profile."""

#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the user."""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0

#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)

#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print("\nWelcome back, " + self.username + "!")

#     def read_login_attempts(self):
#         print("\nLogin attempts: " + str(self.login_attempts))

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

from user_info import User

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print("\nPrivileges:")
		for privilege in self.privileges:
			print("-" + privilege)

# julie = Admin('Haoyu', 'Zhu', 'julie', 'julie@example.com', 'tianjin')
# julie.privileges.show_privileges()

