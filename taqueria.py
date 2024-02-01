# Program that prompt user for food order and computes total

# Store dictionary of menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Prompt user for order with loop until they end program
full_order = []
while True:
    try:
        order = input("Item: ")

        # Convert user input to titlecase to match dictionary str
        order = order.title()

        # See if input matches in dictionary then store price in a list
        if order in menu:
            full_order.append(menu[order])
            total = sum(full_order)
            # Format sum to 2 decimal places
            # Output Total
            print(f"Total: ${total:.2f}")
        else:
            continue
    except EOFError:
        # Once the order is done, add all ints in list
        total = sum(full_order)
        # Format sum to 2 decimal places
        # Output Total
        print(f"\nTotal: ${total:.2f}")
        break