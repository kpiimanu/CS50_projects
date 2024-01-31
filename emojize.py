# Program that takes str input and outputs the emojize version w/ corresponding emoji

import emoji


# Function to convert input str into emojize
def str_to_emojize(og_str):
    new_str = emoji.emojize(og_str, language="alias")
    print("Output: " + new_str)


def main():
    # Prompt user to input str
    og_str = input("Input: ")
    str_to_emojize(og_str)


main()