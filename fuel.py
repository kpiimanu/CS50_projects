# Program that prompts for fraction and outputs a percentage

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    percentage = int(percentage)
    result = gauge(percentage)
    print(result)


def convert(fraction):
    # Separate input into list for conversion later
    fraction = fraction.split(sep="/")

    # Convert str in list to int in list
    for i in range(0, len(fraction)):
        fraction[i] = int(fraction[i])

    # Store variables for ints
    numerator = fraction[0]
    denominator = fraction[1]

    # Check for zero division error
    if denominator == 0:
        raise ZeroDivisionError

    # Check if numerator is greater than denominator
    if numerator > denominator:
        raise ValueError

    # Compute
    percentage = (numerator / denominator) * 100
    percentage = round(percentage)
    percentage = int(percentage)
    return percentage

def gauge(percentage):
    # Check if percentage is already an integer
    if isinstance(percentage, int):
        percent_int = percentage
    else:
        percent_int = int(percentage.strip('%'))

    # Sort through fuel gauge full vs empty vs other
    if percent_int <= 1:
        return("E")
    elif percent_int >= 99:
        return("F")
    else:
        # Output percent
        return(f"{percent_int}%")


if __name__ == "__main__":
    main()