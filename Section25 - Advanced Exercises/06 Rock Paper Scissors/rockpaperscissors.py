#Rock Paper Scissors Game

#The user choose his/hers options
#Computer choose randonmly

#Result
#Scissors beats paper
#Paper beats rock
#Rock beats scissors


import random

def rock_paper_scissors_game():
    print ("****** Welcome to Rock, Paper, Scissors Game ******")
    user_choice = input("Please, insert your choice: rock, paper or scissors: ")
    while user_choice.lower() not in ['rock' , 'paper', 'scissors']:
        print("Please, insert a valid option. Make sure you haven't mistyped")
        user_choice = input("Please, insert your choice: rock, paper or scissors: ")
    
    if user_choice == 'rock' or 'paper' or 'scissors':
        machine_choice = random.choice(["rock" , "paper" , "scissors"])
        if user_choice == machine_choice:
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have tie!")

        elif(user_choice=='rock' and machine_choice=='paper'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have lost!")
        elif(user_choice=='rock' and machine_choice=='scissors'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have won!")

        elif(user_choice=='paper' and machine_choice=='scissors'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have lost!")       
        elif(user_choice=='paper' and machine_choice=='rock'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have won!")
        
        elif(user_choice=='scissors' and machine_choice=='rock'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have lost!")
        elif(user_choice=='scissors' and machine_choice=='paper'):
            print(f"Machine threw a {machine_choice}, and you a {user_choice}. You have won!")

        return "Come back for more!"

print (rock_paper_scissors_game())
