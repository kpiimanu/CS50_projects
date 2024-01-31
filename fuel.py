# Program that prompts for fraction and outputs a percentage

# Request input from user as a fraction
while True:
    try:
        fuel = input("Fraction: ")

        # Separate input into list for conversion later
        fuel = fuel.split(sep="/")

        # Convert str in list to int in list
        for i in range(0, len(fuel)):
            fuel[i] = int(fuel[i])

        # Store variables for ints
        numerator = fuel[0]
        denominator = fuel[1]

        # Check for zero division error
        if denominator == 0:
            raise ZeroDivisionError

        # Check if numerator is greater than denominator
        if numerator > denominator:
            raise ValueError

        # Compute
        fuel_percent = (numerator / denominator) * 100
        fuel_percent = round(fuel_percent)


        # Sort through fuel guage full vs empty vs other
        if fuel_percent <= 1:
            print("E")

            # Exit loop
            break
        elif fuel_percent >= 99:
            print("F")

            # Exit loop
            break
        else:
            # Output percent
            print(f"{fuel_percent}%")

            # Exit loop
            break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue