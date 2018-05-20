class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def read_login_attempts(self):
        print("\nLogin attempts: " + str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()
# eric.read_login_attempts()
# eric.increment_login_attempts()
# eric.increment_login_attempts()
# eric.read_login_attempts()
# eric.reset_login_attempts()
# eric.read_login_attempts()


# willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
# willie.describe_user()
# willie.greet_user()

