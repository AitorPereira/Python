#Null Values - NaN

from operator import index
import pandas as pd
import numpy as np

#np.nan to create a null element

values_list = ['1','2',np.nan,'4']
print (values_list)
#['1', '2', nan, '4']

serie = pd.Series (values_list, index=list('abcd'))
print (serie)
#a      1
#b      2
#d      4
#c    NaN

#To return if an element is null (True or False)
serie.isnull()
# a    False
# b    False
# c     True
# d    False

#To remove all nulls elements
serie.dropna()
# a    1
# b    2
# d    4

values_list = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]
print (values_list)
#[[1, 2, 3], [4, nan, 5], [6, 7, nan]]

index_list = list('123')
columns_list = list('abc')

dataframe = pd.DataFrame(values_list, index=index_list, columns=columns_list) #type: ignore
print (dataframe)
#    a    b    c
# 1  1  2.0  3.0
# 2  4  NaN  5.0
# 3  6  7.0  NaN

dataframe.isnull()
#        a      b      c
# 1  False  False  False
# 2  False   True  False
# 3  False  False   True

dataframe.dropna()
#    a    b    c
# 1  1  2.0  3.0

#To replace nulls with a number
dataframe.fillna(0)
#    a    b    c
# 1  1  2.0  3.0
# 2  4  0.0  5.0
# 3  6  7.0  0.0

#We use this command to enable the option to operate with the dataframe