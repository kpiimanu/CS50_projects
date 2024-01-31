# Program that outputs a specific quantum of $ depending on the greeting

# Ask for greeting from user
greeting = input("Please enter your greeting message: ")


# Remove white space from str and make lowercase
greeting = greeting.lower().strip()


# Assign $ depending on greeting and if str begins with letter h
if greeting == "hello" or greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")