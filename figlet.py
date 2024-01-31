# Program that takes str input and outputs in desired figlet text font

import sys
import random
from pyfiglet import Figlet

# Created name for  figlet library
figlet = Figlet()


# Zero arguments - random font output. Check if true
if len(sys.argv) == 1:
    random_font = True


# Two arguments - output a specific font. False
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    random_font = False

else:
    print("Invalid usage")
    sys.exit(1)


# Function to retrieve font type
figlet.getFonts()

# Choose specific font entered in terminal for text
if random_font == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    font = random.choice(figlet.getFonts())

text = input("Input: ")

# Print result
print("Output: ")
print(figlet.renderText(text))