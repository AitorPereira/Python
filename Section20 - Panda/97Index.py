from operator import index
import pandas as pd
import numpy as np

values_list = np.random.randn(6)
print (values_list)

#This will create a double index
index_list = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
serie = pd.Series(values_list, index=index_list)
print (serie)
# 1  a   -1.131794
#    b    1.215545
#    c   -0.550183
# 2  a    1.460280
#    b   -0.236996
#    c    0.974629

#To select only index 1 elements
serie[1]
# a   -0.131794
# b    1.215545
# c   -0.550183

#To select only index 1 elements and subindex b element
print (serie[1]['b'])
# 1.215545

#To replace subindex for columns
dataframe = serie.unstack()
print (dataframe)
#           a         b         c
# 1 -1.131794 -1.349815  0.481254
# 2  0.103220  0.806963  0.102548

values_list2 = np.arange(16).reshape(4,4)
index_list2 = list('1234')
column_list2 = list('abcd')

dataframe2 = pd.DataFrame(values_list2, index=index_list2, columns=column_list2) #type: ignore
print (dataframe2)
#     a   b   c   d
# 1   0   1   2   3
# 2   4   5   6   7
# 3   8   9  10  11
# 4  12  13  14  15

#Now to create a serie with DOUBLE INDEX
serie2 = dataframe2.stack()
print (serie2)
# 1  a     0
#    b     1
#    c     2
#    d     3
# 2  a     4
#    b     5
#    c     6
#    d     7
# 3  a     8
#    b     9
#    c    10
#    d    11
# 4  a    12
#    b    13
#    c    14
#    d    15