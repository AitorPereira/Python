import random


cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
symbol = ["J", "Q", "K"]
figures = ["J", "Q", "K", "A"]
cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


print("♠♣♦♥ Welcome to Blackjack Game ♠♣♦♥")

answer=input("\n Do you want to play?")

while answer.lower() not in ["yes", "no"]:
    print("Please, make sure you type 'Yes' or 'No' correctly")
    answer = input("\n Do you want to play?")

if answer.lower() == "yes":
    self_card1 = random.choice(cards)
    self_card2= random.choice(cards)
    oponent_card1 = random.choice(cards)
    oponent_card2 = random.choice(cards)

    if self_card1 == "A" and self_card2 == "A":
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 11
        self_card2 = 1
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")
        print(f"First Oponent Card: {oponent_card1}")



    elif (self_card1 == "A" and self_card2 in symbol):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 11
        self_card2 = 10
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")
        print("Congratulations! You have won")

    elif (self_card1 in symbol and self_card2 == "A"):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 10
        self_card2 = 11
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")
        print("Congratulations! You have won")

    elif (self_card1 == "A" and self_card2 not in figures):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 11
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif (self_card1 not in figures and self_card2 == "A"):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card2 = 11
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif (self_card1 in symbol and self_card2 in symbol):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 10
        self_card2 = 10
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif (self_card1 in symbol and self_card2 not in figures):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card1 = 10
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif (self_card1 not in figures and self_card2 in symbol):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_card2 = 10
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif (self_card1 not in figures and self_card2 not in figures):
        print(f"Your cards are: {self_card1}, {self_card2}")
        self_total_punctuation = int(self_card1) + int(self_card2)
        print(f"Your total punctuaction is: {self_total_punctuation}")


elif answer.lower() == "no":
    print ("No problem! Come back again")


def more_cards(self_card1, self_card2):
    answer2 = input("Do you want more cards? Type 'yes' or 'no' ")
    while answer2.lower() not in ["yes", "no"]:
        print("Please, make sure you type Yes or No correctly")
        answer2 = input("Do you want more cards? Type 'yes' or 'no' ")
    if answer.lower() == "yes":
        self_card3= random.choice(cards)
        print(f"Your cards are: {self_card1}, {self_card2}, {self_card3}")
        if self_card3 in symbol:
            self_card3=10
        elif self_card3 is "A"xºxº 
        
        print(f"Your total punctuaction is: {self_total_punctuation}")

    elif answer.lower() == "no":
        print ("No problem! Come back again")

