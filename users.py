# Make a class called User w/ 2 attributes: first_name & last_name
# Also create several other attributes for a user_profile

class User:
    def __init__(self, first_name, last_name, gender, email, phone_number, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = login_attempts
    """Make a method called describe_user() that prints a personalized greeting to the user"""
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Aloha {full_name}! Welcome back.")

    """ A method that increments the value of login_attempts by 1"""
    def increment_login_attempts (self, login_attempts=1):
        self.login_attempts =+ login_attempts
        print(f"There have been {self.login_attempts} login attempts by your user.")

    """ A method that resets the value of login attempts to 0"""
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

"""Create several instances representing different users, and call both methods for each user"""
taylor_swift = User("Taylor", "Swift", "Female", "taylor@example.com", "123-456-7890", 6)
travis_kelce = User("Travis", "Kelce", "Male", "tntn@example.com", "987-654-3210", 10)

print('')
taylor_swift.describe_user()
taylor_swift.increment_login_attempts(6)
taylor_swift.reset_login_attempts()
print('')
travis_kelce.describe_user()
travis_kelce.increment_login_attempts(10)
travis_kelce.reset_login_attempts()
print('')
