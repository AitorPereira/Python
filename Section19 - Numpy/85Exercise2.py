#Exercise
#1.	Create a list with numbers from 10 to 19
#2.	Create another list with numbers from 50 to 59
#3.	Create a 2x10 matrix using the previous two lists
#4.	Create another matrix whose values are equal to the previous matrix multiplied by 2

import numpy as np

#Exercise 1 & 2
list1 = np.arange(10,20)
list2= np.arange(50,60)

#Exercise 3
double_list = (list1, list2)
print (double_list)

matrix = np.array (double_list)
print (matrix)

shape = matrix.shape
print (shape)

#Exercise 4
matrix_double = matrix * 2
print (matrix_double)

