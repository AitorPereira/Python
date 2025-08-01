import numpy as np
array = np.arange(5)
print (array)

#We use sqrt to calculate the square root of the numbers within the array
np.sqrt(array)
#[0.         1.         1.41421356 1.73205081 2.        ] - This is the result when printing

#To generate random numbers we use np.random.rand(number)
np.random.rand(5)
#[0.         1.         1.41421356 1.73205081 2.        ] - This is the result when printing

#To transform a list to an array we use np.array(list)
list = [5,6,7,8,9]
array2 = np.array(list)

#To add multiple arrays we use np.add (array,array2) 
addition_arrays = np.add(array,array2)
print (addition_arrays)
#[ 5  7  9 11 13] - This is the result when printing

#To pick the higher numbers from the same positions in two arrays, we use np.maximum(array1, array2)
maximum_arrays = np.maximum(array, array2)
print (maximum_arrays)
#[5 6 7 8 9] - This is the result when printing



