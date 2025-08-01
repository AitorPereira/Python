#Operators with arrays (+,-,+,/,**)

import numpy as np

array1 = np.array([1,2,3,4])

#We use array1 + 4 to add 4 to all the list
add = array1 + 4
print (add)

#We use array1 - 3 to subtract 3 from all the list
subtract = array1 - 3
print (subtract)

#We use array1 + 2 to multiply all the list by 2
multiply = array1 * 2
print (multiply)

#We use array1 / 2 to divide all the list by 2
divide = array1 / 2
print (divide)

#We use array1 ** 3 to square all the list
square = array1 ** 3
print (square)

#We use array1 % 2 to get the remainder of the list (modulus)
modulus = array1 % 2
print (modulus)

#All of these operators does not register data on the variable, the results of these operators are merely for printing

#If you want to actually upload the data we would have to use
array1 = array1 + 4
print (array1)

#To add 2 lists into a single array we need to use np.array(double_list)
list1=[1,2,3,4]
list2=[5,6,7,8]
double_list = (list1,list2)
double_array = np.array(double_list)
print (double_array)

#Then we can use operators with these arrays in the same way as before. For example:
result = double_array + 5
print (result)

#and if we want to actually upload the data into the variable:
double_array = double_array * 2
print (double_array)

