# Program that takes user to input of text and outputs a corresponding reading level

from cs50 import get_string

text = get_string("Text: ")
# Count number of letters in text ( all are upper + lowercase)


def count_letters(text):
    letters = 0
    # Starts at 1 since we will count the spaces to rep number of words
    words = 1
    sentences = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        elif text[i] == " ":
            words += 1
        elif text[i] in [".", "!", "?"]:
            sentences += 1

    # Calculate average number of letters per 100 words store as L
    L = letters / words * 100
    S = sentences / words * 100
    # Input L into Coleman-Liau index equation (0.0588 * L - 0.296 * S - 15.8) to compute reading level
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print reading level ("Grade: X"). If X < 1 print: "Before Grade 1". If x > 16 print: "Grade 16+"
    # Grade level below first
    if index < 1:
        print("Before Grade 1")
    # Grade level above 16
    elif index > 16:
        print("Grade 16+")
    # Grade levels between 1 & 16
    else:
        print("Grade ", index)


count_letters(text)