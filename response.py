# Program that prompts user for email and identifies whether it is valid or not

from validator_collection import validators
from validator_collection.errors import EmptyValueError, InvalidEmailError


def main():
    print(email_validation(input("What's your email address? ")))


# Function to validate an email
def email_validation(s):
    try:
        # Check if email entered is in a valid format and dont allow blank input
        email_address = validators.email(s, allow_empty=False)
        return "Valid"
    except EmptyValueError:
        return "Invalid"
    except InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()