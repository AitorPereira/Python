#Create a variable "minimum" with the value 20  
#Create a variable "maximum" with the value 500  
#Get a value from the keyboard and store it in the variable "data"  
#Convert the variable "data" to a number and store it in the variable "num"  
#If "num" is less than the value of "minimum", display the text "Low value"  
#If "num" is greater than the value of "maximum", display the text "High value"  
#If "num" is between the value of "minimum" and "maximum", display "Medium value"

minimum = 20
maximum = 500

data = input("Insert a number")
num = int(data)

if num < minimum:
    print ("Low Value")
elif num > maximum:
    print ("High Value")
else:
    print ("Medium Value")