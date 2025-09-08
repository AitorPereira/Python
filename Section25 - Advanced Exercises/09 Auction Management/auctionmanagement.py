# Auction program to calculate the highest bid
# Workflow:
# - Display a welcome message for the auction program
# - Ask for the name of the first bidder
# - Ask for the amount of their bid
# - Add the name (key) and their bid (value) to a bids dictionary
# - Clear the screen
# - Ask if there are more people who want to place a bid (yes/no) (loop until answer is "no")
#   If answer == "yes":
#       - Ask for the next bidder's name
#       - Ask for their bid
#       - Add the name (key) and bid (value) to the original bids dictionary
#       - Clear the screen
#   If answer == "no":
#       - Show the winning bid (the highest bid in the dictionary)
#       - End the program

import os

bids={}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def auction_management(bids):
    print("Hi everyone and Welcome to the best auction in the world.")
    print("Article n1: Monalisa Paint from Louvre")

    name_bidder = (input("What's your name: "))
    while True:
        try:
            amount_bid = float(input("What's your bid for the 1st amazing article (USD): "))
            break
        except ValueError:
            print("Please type only numbers")

    bids[name_bidder] = float(amount_bid)

    clear()

    more_bids = str(input("Are there more people who want to place a bid? (Yes/No): "))

    while more_bids.lower() != 'no':
        if more_bids.lower() == 'yes':
            name_bidder = (input("What's your name: "))

            while True:
                try:
                    amount_bid = float(input("What's your bid for the 1st amazing article (USD): "))
                    break
                except ValueError:
                    print("Please type only numbers")

            bids[name_bidder] = float(amount_bid)

            clear()

        else:
            print("I can't understand, please type yes or no")
        
        more_bids = str(input("Are there more people who want to place a bid? (Yes/No): "))

    winner = max(bids, key=bids.get)
    return (f"The winner is {winner} with a bid of ${bids[winner]}")

print(auction_management(bids))