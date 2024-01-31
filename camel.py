# Program that converts camelCase into snakecase

# Request for user input of camelCase
string = input("Please enter camelCase here: ")

# For every capital letter in str replace with _ and then add that same letter as lowercase
for i in string:
    if i.isupper():
        string = string.replace(i, "_" + i.lower())

# Output the conversion
print(string)