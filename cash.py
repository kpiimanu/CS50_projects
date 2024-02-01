# Program to determine minimum number of coins given for exact change

from cs50 import get_float


def coin_counting(change_owed):
    # Set coin cointer to 0
    coin_count = 0

    # Convert input amount into cents and round
    change_cents = round(int(change_owed * 100))

    # Coin count
    while change_cents > 0:
        while change_cents >= 25:
            change_cents -= 25
            coin_count += 1
        while change_cents >= 10:
            change_cents -= 10
            coin_count += 1
        while change_cents >= 5:
            change_cents -= 5
            coin_count += 1
        while change_cents >= 1:
            change_cents -= 1
            coin_count += 1
    return coin_count


# Prompt user for change owed - If input is negative, re-prompt; otherwise break
while True:
    change_owed = get_float("How much is your change? ")
    if change_owed > 0:
        break
# Execute coin counting function
coin_count = coin_counting(change_owed)

# Print the number of coins used for giving change
print(coin_count)