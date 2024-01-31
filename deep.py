# Program that asks user for the answer to the great question of life

# Ask for input from the user keep as str
answer = input("What is the answer to the great question of life, the universe, and everything? ")

# Convert str to lowercase and remove any white space
answer = answer.lower().strip()

# Check to see if the user says 42 numerically or written out
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")