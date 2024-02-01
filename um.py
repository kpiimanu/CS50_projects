# Program that counts the number of um's used in a str and outputs value as int

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Use findall to locate each time the work 'um' is used in input
    # RE ensures um cannot be used in a word...only as a stand alone
    um_list = re.findall(r"\bum\b", s.lower())
    counter = 0
    for _ in um_list:
        counter += 1

    return counter


if __name__ == "__main__":
    main()
