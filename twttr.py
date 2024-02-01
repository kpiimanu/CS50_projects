# Program that prompts user for str and will output omitting all vowels

# Function created to remove vowels in string
def shorten(word):
    # List of vowels in capital and lowercase to reference for removal
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    # variable to store empty str
    new_text = ""
    # Looping through each char in str
    for letter in word:
        if letter not in vowels:
            # As long as char is not a vowel, it is added to the new_text variable
            new_text += letter
    return new_text

# Main
def main():
    # Prompt user input for str
    word = input("Input: ")
    # Pass through remove_vowel function and store in new variable
    # Check if input contains numeric or punctuation characters
    updated_text = shorten(word)
    # Output updated str
    print(f"Output: {updated_text}")


if __name__ == "__main__":
    main()