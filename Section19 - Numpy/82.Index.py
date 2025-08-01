import numpy as np

array = np.arange(0,11)
print (array)

array[0:3]
#[0 1 2] - Prints 3 positions

array[:]
#[ 0  1  2  3  4  5  6  7  8  9 10] - Print the whole array

array[-10:]
#To print the last 10 digits of an array

copy_array = array.copy()
#[ 0  1  2  3  4  5  6  7  8  9 10] - Print a copy of the array

copy_array[0:3] = 20
#[20 20 20  3  4  5  6  7  8  9 10] - Replace the first 3 positions by the number 20

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
#[[1 2 3] - This creates 3 lists in 3 raws and 3 columns
# [4 5 6]
# [7 8 9]]

#To select any specific list or raw from the array:
array2[0]
#[1 2 3] - This will print the first raw since is the first position
array2[1]
#[1 2 3] - This will print the second raw since is the second position
array2[2]
#[1 2 3] - This will print the third raw since is the third position

#To select any specific number from the array:
print (array2[1][0])
#4 - This will only select the first raw and the column zero. Remember every number starts in 0

