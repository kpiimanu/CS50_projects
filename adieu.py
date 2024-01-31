# Program to prompt user to input names to bid adieu
import inflect

# Variables for inflect and a list for names
p = inflect.engine()
names = []

# Loop to continuously prompt for name input until user ends program
while True:
    try:
        # Promt user to enter a name using a loop until user ends via control + d
        # Store each name into list using inflect - p.join()
        names.append(input("Names: "))

        # Make an exception for EOFError w/ conditionals for number of names
    except EOFError:
        if len(names) == 1:
            all_names_format = p.join(names, final_sep="")
            print(f"Adieu, adieu, to {all_names_format}")
            break
        elif len(names) == 2:
            all_names_format = p.join(names, final_sep="")
            print(f"Adieu, adieu, to {all_names_format}")
            break
        elif len(names) == 3:
            all_names_format = p.join(names, final_sep=",")
            print(f"Adieu, adieu, to {all_names_format}")
            break
        else:
            all_names_format = p.join(names, final_sep=",")
            print(f"Adieu, adieu, to {all_names_format}")
            break