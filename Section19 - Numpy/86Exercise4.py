#import numpy as np

#Create a function that uses numpy to add two list of numbers

#def sum_numpy_arrays(array1, array2):
# Example of use
#array1 = [1, 2, 3, 4, 5]
#array2 = [5, 4, 3, 2, 1]

#result = sum_numpy_arrays(array1, array2)
#print("Sum result:", result)

import numpy as np

list1 = np.arange(1,6)
list2 = np.arange (5,0,-1)

def addition(list1,list2):
    add = np.add(list1,list2)
    return add

print_addition = addition(list1,list2)
print (print_addition)
