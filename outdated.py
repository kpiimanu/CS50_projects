# Program that converts the date input by user into ISO 8601

import re

# Dict that stores name of the months
month_name = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    # Prompt user to enter date and remove any leading or trailing white space to prep for regex
    date = input("Date: ").strip()

    # Validate input format using regular expressions (regex) to ensure splitting has correct order of values
    # Regex includes 2 patterns. first is for Month Day, Year
    # Second pattern is for MM/DD/YYYY. The regex also accounts for quotation marks used in input
    date_pattern = re.compile(r'^"?(\w+\s+\d{1,2},\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})"?$')

    # If the input does not match the regex, reprompt user
    if not date_pattern.match(date):
        continue

    # if a / is in input, splitting string accordingly and convert into int
    if "/" in date:
        date_separation = date.split("/")
        day = int(date_separation[1])
        month = int(date_separation[0])
        year = int(date_separation[2])

        # Check that the value for month does not exceed 12
        if month > 12:
            continue
        # Check that the value for day does not exceed 31
        if day > 31:
            continue
    else:
        # Account for date entered using comma
        raw_date = date.split(" ")
        day = int(raw_date[1].strip(","))
        month = month_name.get(raw_date[0].title())
        year = int(raw_date[2])

    if day > 12 and month <= 12:
        continue

    # Ensure layout for ISO 8601, as well as include a 0 before month and day
    iso_date = f"{year}-{month:02d}-{day:02d}"
    print(iso_date)
    break