#Create a variable "string" that contains "This is just an example"
#Create a variable "length" that contains the length of the variable string
#Create a variable "strlength" that contains the value of length but converted into a string
#Create a variable "upper" that contains the variable string in uppercase
#Create a variable "result" that concatenates "upper" with the text "has a length of " and "strlength"

string = "This is just an example "

length = len(string)

strlength = str(length)

upper = string.upper()

result = upper + "has a lenght of " + strlength
print (result)

print (f"{upper} has a lenght of {strlength}")


string2 = "This is just an example"
length2 = len(string2)
strlength2= str(length2)
upper2 = string2.upper()
result2 = upper2 + "has a lenght of " + strlength2 