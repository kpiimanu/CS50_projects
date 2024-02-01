# Program that outputs a specific quantum of $ depending on the greeting


def main():
    greeting = input("Please enter your greeting message: ")
    amount = value(greeting)
    print(f"${amount}")

# Function that determines amount of $ distributed based on greeting
def value(greeting):
    greeting = greeting.lower().strip()
    # Assign $ depending on greeting and if str begins with letter h
    if greeting == "hello" or greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()