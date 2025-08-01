#Replace the rows with columns
import numpy as np

#We will create an array from 0 to 14
#And we will create 3 raws and 5 columns by using .reshape
array = np.arange(15).reshape((3,5))
print (array)

#Now to print a single element of the list we will proceed by:
array[1][1]
#6 - This is the item we have picked. Remember all rows and columns start from 0

#Now to reorganize raws for columns and viceversa:
array_tras = array.T
print (array_tras)