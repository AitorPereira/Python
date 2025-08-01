from operator import index
import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])
print (serie1)

serie2 = pd.Series([3,4,5,6], index=['a','b','c','d'])
print (serie2)

solution = serie1 + serie2
print (solution)

values_list = np.arange(4).reshape(2,2)
print (values_list)

# To create a list in a different way, we will use the list command and write the names together.
# It will automatically split them into individual elements.
index_list = list('ab')
#['a', 'b']

column_list = list('12')
#['1', '2']

dataframe1 = pd.DataFrame(values_list, index=index_list, columns=column_list) #type: ignore
print (dataframe1)
#   1  2
#a  0  1
#b  2  3

values_list2 = np.arange(9).reshape(3,3)

index_list2 = list('abc')
column_list2 = list ('123')
dataframe2 = pd.DataFrame (values_list2, index= index_list2, columns = column_list2) #type: ignore
print (dataframe2)

# When we add a 2x2 and a 3x3 DataFrame, only the values with matching row and column labels will be added.
# The rest will return NaN (null) where there is no match.
""" dataframe3 = dataframe1 + dataframe2
print (dataframe3) """

#To avoid nulls values, we can use the fill_value parameter.
dataframe1.add(dataframe2, fill_value=0)
#     1    2    3
#a  0.0  2.0  2.0
#b  5.0  7.0  5.0
#c  6.0  7.0  8.0