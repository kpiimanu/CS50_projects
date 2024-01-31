# Program that outputs number of lines in a program (1 command line arg)

import sys


# Main function going through commandline req, checking valid python file, then counting lines
def main():
    cmdline_check()
    py_file()
    line_count()


# Function to check command-line info (must be 1 arg only)
def cmdline_check():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(2)


# Function to check if file ends in .py
def py_file():
    program = []
    program.append(sys.argv[1])
    program = program[0].split(sep=".")
    if program[-1] != "py":
        print("Not a Python file")
        sys.exit(3)


# Function to count lines of file
def line_count():
    count = 0
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(4)

    for line in lines:
        if line.lstrip().startswith("#"):
            pass
        elif line.isspace():
            pass
        else:
            count += 1
    print(count)


if __name__ == "__main__":
    main()