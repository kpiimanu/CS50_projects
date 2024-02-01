# Program that user is faced with 10 set of math questions and score of correct answers

import random


def main():
    # Variable set for get_level function to use in main code
    level = get_level()

    # Starting points at 0 and will add with each correct response
    points = 0

    # 10 problems total used in for loop to iterate
    problems = 10
    for _ in range(problems):
        # Running generate_integer function to return random int for x & y accroding to level
        x, y = generate_integer(level)
        # Displaying equation to user to answer
        response = input(f"{x} + {y} = ")
        answer = x + y

        # Checking if user response is correct
        if int(response) == answer:
            points += 1
        else:
            attempts = 1
            # User has only 3 attempts to enter correct response
            while int(response) != answer and attempts < 3:
                print("EEE")
                response = input(f"{x} + {y} = ")
                attempts += 1
                if attempts == 3:
                    print(f"{x} + {y} = {answer}")
                    break
            if int(response) == answer:
                points += 1

    # Final score displayed
    print(f"Score: {points}")


# Function to prompt user for a level & returns the level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            continue


# Function that returns a randomly generated non_negative int
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()