#Print on the screen the text "Enter the first number"
#Create the variable data1 with the first value entered in the previous step
#Print on the screen the text "Enter the second number"
#Create the variable data2 with the first value entered in the previous step
#Convert the variable data1 into a numeric variable called number1
#Convert the variable data2 into a numeric variable called number2
#Create the variable sum with the sum of number1 and number2
#Convert the variable sum into a text variable called strSum
#Create the variable result with the concatenation of "The sum is " and strSum
#Print the value of result

data1= input ("Enter the first number ")
data2= input ("Enter the second number ")
number1 = int(data1)
number2 = int(data2)
sum = number1 + number2
strSum = str(sum)
result = "The sum is " + strSum

print (result)
print (f"The sum of {data1} and {data2} is the total amount of {sum}")
print ("The sum of {} and {} is the total amount of {}".format(data1,data2,sum))