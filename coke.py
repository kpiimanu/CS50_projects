# Program to prompt user to insert a coin towards a Coke

# Function to vet coin amount
# Function to vet coin amount
def coin_accept(amount):
    if amount == 25 or amount == 10 or amount == 5:
        return True
    else:
        return False

# Prompt user to input one coin (either 25, 10 or 5 cents)
while True:
    amount = int(input("Insert Coin: "))
    if coin_accept(amount):
        break
    else:
        print("Amount Due: 50")
        continue

coin_accept(amount)
i = 0 + amount

# while amount in machine is less than 50, prompt user to insert another coin and display amount due
while i < 50:
    print(f"Amount Due: {50 - i}")
    amount = int(input("Insert Coin: "))
    coin_accept(amount)
    i = i + amount

# Once amount is => 50 cents, output change owed
if i >= 50:
    print(f"Change Owed: {i - 50}")