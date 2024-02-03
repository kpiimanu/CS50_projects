# Make a list that contains a series of 10 numbers and 5 letters

from random import choice

lotto_list = [1,2,3,4,5,6,7,8,9,10,'a','e','m','f','k']
winning_ticket = []
"""Randomly select 4 numbers or letters from the list and print any ticket that matches this wins a prize"""
counter = 0
while counter < 4:
    pick = choice(lotto_list)
    winning_ticket.append(pick)
    counter += 1

print(f"The ticket that matches {winning_ticket} wins a prize!")
