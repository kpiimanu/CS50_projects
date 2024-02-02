# Make a class called User w/ 2 attributes: first_name & last_name
# Also create several other attributes for a user_profile

class User:
    def __init__(self, first_name, last_name, gender, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
    """Make a method called describe_user() that prints a personalized greeting to the user"""
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Aloha {full_name}! Welcome back.")

"""Create several instances representing different users, and call both methods for each user"""
taylor_swift = User("Taylor", "Swift", "Female", "taylor@example.com", "123-456-7890")
travis_kelce = User("Travis", "Kelce", "Male", "tntn@example.com", "987-654-3210")

print('')
taylor_swift.describe_user()
print('')
travis_kelce.describe_user()
print('')