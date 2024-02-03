# Write a clas called Admin that inherits from the User class

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
    
class Admin(User):
    def __init__(self, first_name, last_name, gender, email, phone_number, login_attempts):
        super().__init__(first_name, last_name, gender, email, phone_number, login_attempts)
        """Add an attribute called 'priviledges' that stores a list of strings"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

"""Write a separate Privileges class"""
class Privileges(User):
    def __init__(self, first_name, last_name, gender, email, phone_number, login_attempts):
        super().__init__(first_name, last_name, gender, email, phone_number, login_attempts)
        """Add an attribute called 'priviledges' that stores a list of strings"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    """Write a method called show_privileges() that list admins set of privileges"""
    def show_privileges(self):
        print(f"The Admins set of privileges include: {self.privileges}")

"""Create an instance of admin and call your method"""
admin_privileges = Privileges('Wonder', 'Woman', 'Female', 'ww@example.com', '909-098-9999', 69)
print(admin_privileges.show_privileges())
