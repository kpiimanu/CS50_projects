# Make a class Die with one attribute called sides (default value of 6)
from random import randint

class Die:
    def __init__(self, sides):
        self.sides = 6

    """Write a method called roll_die() that prints random number between 1 & 6"""
    def roll_die(self):
        random_number = randint(1, 6)
        print(f"{random_number}")

"""Make a 6 sided die and roll it 10 times"""
shake_them_die = Die(sides=6)
count = 0
while count < 10:
    shake_them_die.roll_die()
    count += 1