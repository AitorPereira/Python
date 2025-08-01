#Concatenation of arrays, series and dataframes

import pandas as pd #for series and dataframes
import numpy as np #for arrays

array1 = np.arange(9).reshape(3,3)

#To concatenate arrays vertically
array_concatenate = np.concatenate([array1, array1])
print (array_concatenate)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]
#  [0 1 2]
#  [3 4 5]
#  [6 7 8]]

#To concatenate arrays horizontally
array_concatenate = np.concatenate([array1, array1], axis=1)
print (array_concatenate)
# [[0 1 2 0 1 2]
#  [3 4 5 3 4 5]
#  [6 7 8 6 7 8]]

#To concatenate series
serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([4,5,6], index=['d','e','f'])
serie3 = pd.concat([serie1, serie2], keys=['serie1' , 'serie2'])
print (serie3)
# a    1
# b    2
# c    3
# d    4
# e    5
# f    6

dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a','b','c'])
print (dataframe1)
#           a         b         c
# 0  0.434762  0.610633  0.931633
# 1  0.459028  0.352187  0.410732
# 2  0.800614  0.243018  0.206898

dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a','b','c'])
print (dataframe2)
#           a         b         c
# 0  0.936345  0.237593  0.708906
# 1  0.203491  0.824545  0.519934

#To merge a dataframe
dataframe3 = pd.concat([dataframe1,dataframe2])
print(dataframe3)
# 0  0.278342  0.718616  0.816333
# 1  0.154352  0.256857  0.103626
# 2  0.807679  0.260777  0.490277
# 0  0.936345  0.237593  0.708906
# 1  0.203491  0.824545  0.519934

#To merge them and organice it by index
dataframe4 = pd.concat([dataframe1,dataframe2], ignore_index=True)
print (dataframe4)
# a         b         c
# 0  0.354791  0.388354  0.453387
# 1  0.617424  0.271521  0.938042
# 2  0.696715  0.040001  0.564319
# 3  0.992959  0.516586  0.215808
# 4  0.903443  0.849650  0.770107

