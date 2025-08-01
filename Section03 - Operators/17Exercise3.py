#Create a variable called `numbers` containing a list of numbers from 1 to 10 (both included)  
#Display the value of the variable `numbers`  
#Get input from the keyboard and store it in the variable `data`  
#Convert `data` to a numeric value and store it in the variable `number`  
#If the value of `number` is in the list `numbers`, display the message "Yes"  
#If the entered number is not in the list `numbers`, display the message "No"  

numbers = [1,2,3,4,5,6,7,8,9,10]
print (numbers)

data = input("Insert a number ")
number = int(data)

if number in numbers:
    print ("Yes, it's on the list")

if number not in numbers:
    print ("No, it's not on the list")