# build a half pyramid in (#) according to user input on height

from cs50 import get_int

# main function for half pyramid


def main():
    height = get_height()
    # rows of pyramid
    for i in range(height):
        # space in relation to height
        for space in range(height - i - 1):
            print(" ", end="")
        # columns of pyramid
        for j in range(i + 1):
            print("#", end="")

        print()

# request user input on height


def get_height():
    while True:
        n = get_int("Enter pyramid height(1-8 inclusive): ")
        # check user inputs an int 1-8 inclusive
        if n >= 1 and n <= 8:
            return n


main()