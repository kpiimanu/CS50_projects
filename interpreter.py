# Program that prompts for arithmetic expression and calc answer

# Prompt user for arithmetic expression
expression = input("Enter arithmetic expression: ")

# Split input into a list storing as x, y, z
x, y, z = expression.split(" ")

# Convert x & z into int
x = int(x)
z = int(z)

# match statement for y
match y:
    case "+":
        answer = (x + z)
    case "-":
        answer = (x - z)
    case "*":
        answer = (x * z)
    case "/":
        answer = (x / z)

# Format answer to one decimal place
answer = round(answer, 1)
print("{:.1f}".format(answer))