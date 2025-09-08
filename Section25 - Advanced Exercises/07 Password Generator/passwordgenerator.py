#Password Generator
#Ask for the number of letters, numbers and symbols you want your password to have
#Generate a random password mixing letters, numbers and symbols randonmly

import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+','-','_','=','?','@','^','~','`','|','<','>','/',':',';','.',',','{','}','[',']','(',')','"','\'']

def password_generator(letters,numbers,symbols):
    print ("Welcome to the Password Generator!")

    letters_pw = int(input("How many letters do you want in your password? Insert a number of letters: "))
    print("Thank you, letters added")
    numbers_pw = int(input("How many numbers do you want in your password? Insert a number of numbers: "))
    print("Numbers added")
    symbols_pw = int(input("How many symbols do you want in your password? Insert a number of symbols: "))
    print("Symbols added")

    letter_list=[]
    number_list=[]
    symbol_list=[]

    for letter in range(letters_pw):
        letter_list.append(random.choice(letters))

    for number in range(numbers_pw):
        number_list.append(random.choice(numbers))

    for symbol in range(symbols_pw):
        symbol_list.append(random.choice(symbols))

    password_not_mixed = letter_list + number_list + symbol_list

    #random.shuffle to mix and "".join() to replace list_elements ['A','7','/'] for clean_elements A7/
    random.shuffle(password_not_mixed)
    password_mixed = "".join(password_not_mixed)

    return f"Congratulations! Password has been generated succesfully. \nYour password is: {password_mixed}"


print(password_generator(letters,numbers,symbols))