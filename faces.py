# Program that converts all emoticons into appropriate emoji

# Create convert function that converts emoticon to emoji
def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message


# Create a main function
def main():

    # Prompt user for input
    message = input("Enter expressive message here: ")

    # Pass through convert function
    updated_message = convert(message)


    # Return output
    print (updated_message)


main()