# Program to build a grocery list including a count for each item

# Create 2 empty lists to store grocery items & count of those items
grocery_list = []
count_list = []

while True:
    try:
        # Prompt user to begin entering grocery items one by one & add to list all in uppercase
        grocery_item = input()
        grocery_list.append(grocery_item.upper())

    except EOFError:
        # Once control + d executed
        # Re-order all items in list alphabetically
        grocery_list.sort()

        # Loop through grocery list to build for the count list
        for item in grocery_list:
            count = grocery_list.count(item)
            count_list.append(count)

        # Create a dictionary using both lists
        item_dict = dict(zip(grocery_list, count_list))

        # Print dictionary with the value as prefix
        for key, value in item_dict.items():
            print(value, key)

        break