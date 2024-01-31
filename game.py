# Program that prompts user for a value of n, and then randomly selects a number between 0 & n
import random

while True:
    try:
        # Prompt user to input a value for n (level)
        n = int(input("Level: "))
        if n < 0:
            continue
        else:
            break
    # Ensures that the user inputs a number
    except ValueError:
        continue

# Create a variable that stores a randomly chosen number between 0 & n
random_number = random.randrange(0, n + 1)

# Loop - until user guesses the correct number
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        if guess > n:
            continue
        elif guess < random_number:
            print("Too small!")
            continue
        elif guess > random_number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    # Ensures every guess is a number
    except ValueError:
        continue