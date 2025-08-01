#Create a variable "set" that is a set with the values 1, 2, 3, 4, and 5  
#Display the value of the variable "set"  
#Add the numbers 6, 7, 8, and 9 to the variable "set"  
#Now display the value of the variable "set"  
#Remove the number 9 from the variable "set"  
#Now display the value of the variable "set"  
#Verify the data type of the variable "set" using type()

""" set = {1, 2, 3, 4, 5}
print (set)

#One option
set.update([6,7,8,9])
print (set)

#Second option
set.add(6)
set.add(7)
set.add(8)
set.add(9)
print (set)

set.remove(9)
print (set)

print (type(set)) """

set = {1,2,3,4,5}
print (set)
set.update([6,7,8,9])

set.remove(9)
print (type(set))