import pandas as pd
import numpy as np

values_list = np.arange(9).reshape(3,3)
print (values_list)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

index_list = list('abc')
# ['a', 'b', 'c']

#If we don't pick values for columns will automatically create them as 0,1,2..
dataframe = pd.DataFrame(values_list, index=index_list)
print (dataframe)
#    0  1  2
# a  0  1  2
# b  3  4  5
# c  6  7  8

#Now we want to replace index names for uppercases
new_index = dataframe.index.map(str.upper)
dataframe.index = new_index
print (dataframe)
#    0  1  2
# A  0  1  2
# B  3  4  5
# C  6  7  8

#Another way to replace index names, in this cases by lowercases
dataframe = dataframe.rename(index=str.lower)
print (dataframe)
#    0  1  2
# a  0  1  2
# b  3  4  5


#Another way to replace index names, in this cases by lowercases
dataframe = dataframe.rename(index=str.lower)
print (dataframe)
#    0  1  2
# a  0  1  2
# b  3  4  5
# c  6  7  8

#To replace index names completely 
new_index = {'a':'f', 'b':'g', 'c':'h'}
dataframe = dataframe.rename(index=new_index)
print (dataframe)
#    0  1  2
# f  0  1  2
# g  3  4  5
# h  6  7  8

# To apply changes directly to the original DataFrame without creating a new variable, use inplace=True
new_index = {'f':'j'}
dataframe.rename(index=new_index, inplace=True)
print (dataframe)
#    0  1  2
# j  0  1  2
# g  3  4  5
# h  6  7  8


