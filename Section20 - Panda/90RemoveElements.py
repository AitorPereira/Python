import pandas as pd
import numpy as np

#We can use numpy to create an array of elements and create the index in the moment
np.arange(4)
serie = pd.Series(np.arange(4), index=['a','b','c','d'])
print (serie)

#We use drop to remove any element
print (serie.drop('c'))

values_list = np.arange(9).reshape(3,3)
#[[0 1 2]
# [3 4 5]
# [6 7 8]]

index_list = ['a','b','c']
column_list = ['c1','c2','c3']
dataframe = pd.DataFrame(values_list, index=index_list, columns=column_list) # type: ignore
#   c1  c2  c3
#a   0   1   2
#b   3   4   5
#c   6   7   8

#To remove a raw (only for printing)
print (dataframe.drop('a'))

#To remove a column (only for printing)
print (dataframe.drop ('c1', axis=1))

#To remove data indefinitely
dataframe = dataframe.drop('a')
print (dataframe)