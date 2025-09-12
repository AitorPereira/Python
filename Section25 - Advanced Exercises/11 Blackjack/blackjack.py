import random
import os

def generate_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def sum_cards(cards):
    if sum (cards) == 21 and len(cards) in (2,3,4,5):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def display_winner(self_score, computer_score):
    if self_score == computer_score:
        text = "You tie"
    elif self_score == 0:
        text= "You won! You got 21 BLACKJACK"
    elif computer_score == 0:
        text= "You lost! Computer got 21 BLACKJACK"
    elif self_score > 21:
        text = "You lost. Your score is over 21 "
    elif computer_score > 21:
        text = "You won. Computer got over 21"
    elif self_score > computer_score:
        text = "You won"
    else:
        text = "You lost"
    return text

def clear_screen():
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For MacOS/Linux
    else:
        os.system("clear")

def play():
    print ("We are playing....")

    self_cards = []
    computer_cards = []
    finished = False

    for valor in range(2):
        self_card = generate_cards()
        self_cards.append(self_card)

        computer_card = generate_cards()
        computer_cards.append(computer_card)

    while not finished:
        self_score = sum_cards(self_cards)
        computer_score = sum_cards(computer_cards)

        print (f"Your cards are: {self_cards}. Score = {self_score}")
        print (f"Computer cards are: {computer_cards[0]}")

        if self_score == 0 or computer_score == 0 or self_score > 21:
            self_score = self_score = self_score + 21
            finished = True
        else:
            more_cards = input("Do you want more cards? Answer 'yes' or 'no' ")
            if more_cards.lower() == 'yes':
                self_card = generate_cards()
                self_cards.append(self_card)
                if self_score == 0:
                    self_score = self_score + 21
            else:
                finished = True

    while computer_score != 0 and computer_score < 17:
        computer_card = generate_cards()
        computer_cards.append(computer_card)
        computer_score = sum_cards(computer_cards)
        if computer_score == 0:
            computer_score = computer_score + 21
    print (f"Your cards are: {self_cards}. Score = {self_score}")
    print (f"Computer cards are: {computer_cards}. Score = {computer_score}")

    text = display_winner(self_score, computer_score)
    print (text)


while input("Do you want to play Blackjack? Type 'yes' or 'no': ") == 'yes':
    clear_screen()
    play()



