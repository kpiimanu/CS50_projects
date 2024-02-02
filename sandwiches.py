# A function that accepts a list of items a person wants on a sandwich

def sandwich_order(*filling):
    ingredient_list = []
    for fill in filling:
        ingredient_list.append(fill)
    print(f"\nSandwich order: ")
    for ingredient in ingredient_list:
        print(f" - {ingredient}")

# Call the function 3x
sandwich_order ('mayo', 'turkey', 'cheese')
sandwich_order ('peanut butter', 'jelly')
sandwich_order('tomato', 'mayo')