# Program that user inputs in command-line argument number of bitcoin and outputs total

import requests
import sys

# Command-line specifications at location [1]: must enter a number
if len(sys.argv) == 2:
    try:
        # Variable for number of bitcoin user would like to purchase
        number = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

# Retrieve price of bitcoin as float
try:
    # Retrieve API info on bitcoin
    bitcoin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_dict = bitcoin_info.json()
    # Variable to find the US dollar amount of bitcoin in dictionary
    bitcoin = bitcoin_dict["bpi"]["USD"]["rate_float"]
    # Total amount to purchase bitcoin at specified number input by user
    total_amount = bitcoin * number
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    sys.ext(1)