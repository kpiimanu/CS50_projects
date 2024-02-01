# Program that assesses vanity plate input as valid or invalid per the requirements

# Main function for program
def main():
    plate = input("Plate: ")
    if not plate.isalnum() or (len(plate) < 2 or len(plate) > 6):
        print("Invalid")
        return False

    if is_valid(plate):
        print("Valid")
    else:
        return False

# Function that assesses if input meets all requirements
def is_valid(s):
    if s.isalpha() or s[:2].isalpha() and s[-2:].isnumeric() and s[-2:][0] != "0" and s.isalnum() == True and min_letter_count(s) == True and char_count(s) == True and number_use(s) == True:
        return True
    else:
        return False


# Function to check that plate starts with at least 2 char
def min_letter_count(s):
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    if count >= 2:
        return True
    else:
        return False

# Function to check that plate has more than 2 but no more than 6 char
def char_count(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

# Function to make sure numbers cannot be used in the middle of plate
def number_use(s):
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    return True

if __name__ == "__main__":
    main()