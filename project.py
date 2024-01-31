# Final project - program that acts as a Hawaiian Star Dictionary

import sys
import csv


def main():
    star_name = star_check(input("Star name: "))
    translation = hawaiian_trans(star_name)
    maui_niho(translation)


# Check if input is valid
def star_check(star_name):
    # Check if nothing was entered
    if star_name == "":
        raise ValueError("You must enter a star name")
    # Check if numbers were entered
    if star_name.isnumeric():
        raise ValueError("That is not a valid star name")
    return star_name


# Checking if theres a hawaiian translation for entered star
def hawaiian_trans(star_name):
    # Ensuring capitalization of input matches CSV data
    star_name = star_name.title()

    # Running read_star_data function and storing in variable
    stars = read_star_data()

    # Checking to see if the user input is found in the csv file
    if star_name in stars:
        hawaiian_star = stars[star_name]
        # Storing f-string in variable to use in maui_niho function to include pattern
        translation = (
            f"The Hawaiian star name for '{star_name}' is called {hawaiian_star}."
        )
        return translation
    else:
        raise ValueError("Star not accounted for")


# Read star data from CSV and return a dictionary
def read_star_data():
    stars = {}

    with open("inoa_hoku.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stars[row["English"]] = row["Hawaiian"]

    return stars


# Hawaiian tribal pattern
def maui_niho(translation):
    triforce = [
        "       /\\",
        "      /__\\",
        "     /\\  /\\",
        "    /__\\/__\\",
        "   /\\      /\\",
        "  /__\\    /__\\",
        " /\\  /\\  /\\  /\\",
        "/__\\/__\\/__\\/__\\",
    ]

    # Variable will be used later in code to print alongside tribal pattern
    text = translation

    # Calculate the maximum length of the Triforce symbol
    max_length = max(len(line) for line in triforce)

    # Adjust the length of each line in the Triforce symbol
    triforce = [line.ljust(max_length) for line in triforce]

    # Add space above the Triforce symbol
    print()

    # Print the Triforce symbol and text side by side
    for i in range(len(triforce)):
        print(triforce[i], text if i == len(triforce) // 2 else "")

    # Add space below the Triforce symbol
    print()


if __name__ == "__main__":
    main()