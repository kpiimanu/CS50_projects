# Program that validates if the user inputs a valid IPv4 address or not

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        ip_numbers = ip.split(".")
        for number in ip_numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()