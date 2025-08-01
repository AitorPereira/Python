#Statistics in Dataframe

import pandas as pd
import numpy as np

array = np.array(([1,8,3],[5,6,7]))
print (array)
#[[1 8 3]
#[5 6 7]]

dataframe = pd.DataFrame(array, index=['a','b'], columns=list('123')) #type: ignore
print (dataframe)
#   1  2  3
#a  1  8  3
#b  5  6  7

#To sum by colums
dataframe.sum()
#1     6
#2    14
#3    10

#To sum by raws
dataframe.sum(axis=1)
#a    12
#b    18

#To select the minimum number by columns
dataframe.min()
#1    1
#2    6
#3    3

#To select the minimum number by raws
dataframe.min(axis=1)
#a    1
#b    5

#To select the maximum number by columns
dataframe.max()
#1    5
#2    8
#3    7

#To select the maximum number by raws
dataframe.max(axis=1)
#a    8
#b    7

#To sort out by fewer id number 
dataframe.idxmin()
#1    a
#2    b
#3    a

#To sort out by greater id number 
dataframe.idxmax()
#1    b
#2    a
#3    b

#To obtain statistics from dataframe
print (dataframe.describe())
#              1         2         3
#count  2.000000  2.000000  2.000000 - How many elements are there in each column
#mean   3.000000  7.000000  5.000000 - The average by columns
#std    2.828427  1.414214  2.828427 - The typical deviation 
#min    1.000000  6.000000  3.000000 - The minimum number
#25%    2.000000  6.500000  4.000000 - The 25% of the total addition
#50%    3.000000  7.000000  5.000000 - The 50% of the total addition
#75%    4.000000  7.500000  6.000000 - The 75% of the total addition
#max    5.000000  8.000000  7.000000 - The maximum number

