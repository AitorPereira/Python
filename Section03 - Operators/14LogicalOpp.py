#Logical Operators (and, or, not)

num1 = 10
num2 = 5
num3 = 7
num4 = 8

#and to combine more cases
if (num1 > num2) and (num3 < num4):
    print ("Both conditions are true")
else:
    print ("False")

#to select one of them
if (num1 > num2) or (num3 > num4):
    print ("True")
else:
    print ("False")

#to do the opposite
if not(num1 < num2):
    print ("True")
else:
    print ("False")

