#Creating arrays

import array
import numpy as np

#([0. 0. 0. 0.])
result = np.zeros(4)
print (result)

#([1. 1. 1. 1.])
result2 = np.ones(4)
print (result2)

#([0 1 2 3 4])
result3 = np.arange(5)
print (result3)

#([0 1 2 3 4 5 6 7 8 9])
result4 = np.arange(10)
print (result4)

#([ 2  5  8 11 14 17])
result5 = np.arange(2,20,3)
print (result5)

#list1=[1,2,3,4]
#array[1 2 3 4]
list1=[1,2,3,4]
array1=np.array(list1)
print (array1)
print (list1)

#To unify multiple lists
#([1, 2, 3, 4], [5, 6, 7, 8])   
list1=[1,2,3,4]
list2=[5,6,7,8]
double_list = (list1, list2)
print (double_list)
#We can transform this 2 lists in a single array
double_array = np.array(double_list)
print(double_array)
#To discover this array size we can use .shape
#(2, 4) which is 2 raws and 4 columns
shape = double_array.shape
print (shape)
#to know the data type we have in the array, we use dtype
type = double_array.dtype
print (type)