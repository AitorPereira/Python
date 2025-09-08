# Questions Game
# Select the correct path to escape, otherwise you will fail

def questions_game():
    answer1 = input("You have entered into a Maze full of deadly traps.\n You see a tank full of sharks on your left and a dark room on your right. Choose your path: LEFT/RIGHT ")

    if answer1.lower() == 'right':
        print("Congratulations. You have advanced to the next level!")

        answer2 = input("Multiple vampires are walking towards you. \n You have two options: either swim into a deep pool or wait. Choose your next move: SWIM/WAIT ")

        if answer2.lower() == 'wait':
            print("Well done! You avoided dying eaten by starving piranhas.")

            answer3 = input("The vampires could not find you in the dark room, so they left. \n A secret door opens. \n Inside, you see a table with 3 apples: red, blue, and green. \n Two are poisoned. Choose wisely: BLUE/RED/GREEN ")

            if answer3.lower() == 'green':
                return "AMAZING! You have won the game.\n You escaped and now you are free to live your best life!"
            elif answer3.lower() == 'blue' or 'red':
                return "💀 You have died from poison."
            else:
                return "Invalid choice. Please type LEFT or RIGHT."

        elif answer2.lower() == 'swim':
            return "💀 Sorry, you are piranhas' food. Try again."
        
        else:
            return "Invalid choice. Please type LEFT or RIGHT."
    elif answer1.lower() == 'left':
        return "💀 Sorry, you have been eaten by sharks. Try again."

    else:
        return "Invalid choice. Please type LEFT or RIGHT."


# Game starts here
print("Welcome to the Extreme Question Game!")
print("\nYou need to choose wisely in order to advance. Be careful with your choices.")

answer0 = input("Are you ready to play? Press Y to continue or N to exit: ")

if answer0.lower() == 'y':
    print(questions_game())
else:
    print("Come back when you are ready.")