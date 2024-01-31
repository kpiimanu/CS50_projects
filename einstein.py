# Program that takes input of weight (kg) and outputs energy in joules

# Function for E = m*c2 equation
def equation(mass):

    # Energy equation
    energy = (mass) * (300000000 ** 2)
    return energy


def main():

    # Prompt user to input mass in kg
    mass = input("Please enter mass in kg: ")

    # Convert str to int and save in variable
    mass = int(mass)

    # Use equation function
    energy = equation(mass)

    print(energy)

main()