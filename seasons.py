# Program that prompts user for DOB and then prints how old they are in minutes

from datetime import date
import sys
import inflect

p = inflect.engine()

# Prompt input
# Check format is YYYY-MM-DD
# Calculate how many minutes
# Print in english the answer


def main():
    birth_date = DOB()
    time_difference = calculate(birth_date)
    # Converting number into words omitting "and"
    time_difference = p.number_to_words(round(time_difference), andword="", zero="")
    # Capitalizing first letter
    time_difference = time_difference.capitalize()
    print(f"{time_difference} minutes")


# Function to take the input and convert into time format. raising error if not correctly input
def DOB(birth_date=None):
    if birth_date is None:
        birth_date = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_date)
        return birth_date
    except ValueError:
        print("Invalid date")
        sys.exit(1)



# Function to take birth_date parameter and subtract from todays date converting into minutes
def calculate(birth_date):
    today = date.today()
    time_difference = (today - birth_date).total_seconds() / 60
    return time_difference


if __name__ == "__main__":
    main()