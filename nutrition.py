# Program that propts user for a fruit and outputs calories per serving

# A list of dictionaries to organize fruits and their respected amnt of calories
nutritional_value = [
    {"fruit": "Apple", "calories": "130"},
    {"fruit": "Avocado", "calories": "50"},
    {"fruit": "Banana", "calories": "110"},
    {"fruit": "Cantaloupe", "calories": "50"},
    {"fruit": "Grapefruit", "calories": "60"},
    {"fruit": "Grapes", "calories": "90"},
    {"fruit": "Honeydew Melon", "calories": "50"},
    {"fruit": "Kiwifruit", "calories": "90"},
    {"fruit": "Lemon", "calories": "15"},
    {"fruit": "Lime", "calories": "20"},
    {"fruit": "Nectarine", "calories": "60"},
    {"fruit": "Orange", "calories": "80"},
    {"fruit": "Peach", "calories": "60"},
    {"fruit": "Pear", "calories": "100"},
    {"fruit": "Pineapple", "calories": "50"},
    {"fruit": "Plums", "calories": "70"},
    {"fruit": "Strawberries", "calories": "50"},
    {"fruit": "Sweet Cherries", "calories": "100"},
    {"fruit": "Tangerine", "calories": "50"},
    {"fruit": "Watermelon", "calories": "80"}
]

# Ask user to input fruit
fruit = input("Item: ")
# Convert input to match how its recorded in dictionary list
fruit = fruit.title()

# Loop through list of dictionaries to match input to fruit logged
for item in nutritional_value:
    # If theres a match
    if fruit == item["fruit"]:
        # Print amount of calories
        print("Calories: ", item["calories"])