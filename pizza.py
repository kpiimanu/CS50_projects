# Program that outputs a table formatted as ASCII art

import sys
import csv
from tabulate import tabulate


def main():
    cmd_arg()
    file_check()
    valid_file()


# Function that checks for one command-line arg
def cmd_arg():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(2)


# Check that file name ends in .csv
def file_check():
    csv_file = sys.argv[1]
    if not csv_file.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(3)


# Check if the file exists & print with table
def valid_file():
    file_name = sys.argv[1]
    try:
        with open(file_name) as file:
            csv_data = [row for row in csv.reader(file)]
            print(tabulate(csv_data, headers="firstrow", tablefmt="grid"))
            file.close()
    except FileNotFoundError:
        print("File not found")
        sys.exit(4)


if __name__ == "__main__":
    main()