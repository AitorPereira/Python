#Conditional Statements (if, elif, else)

a = 8
b = 4
c = 7
d = 10

if (a > b):
    print ("True")

if (a < b):
    print ("False")

if (a > c) and (a < d):
    print ("True")
    
#elif is equal to: Check this new statement
if (a > b):
    print ("A is bigger than B")
elif (a == b):
    print ("Equal")
else:
    print ("A is smaller than B")
    
