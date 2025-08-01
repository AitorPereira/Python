#Selecting data in dataframe

import pandas as pd
import numpy as np

values_list = np.arange(25).reshape(5,5)
print (values_list)

index_list = ['i1','i2','i3','i4','i5']
column_list = ['c1','c2','c3','c4','c5']

dataframe = pd.DataFrame (values_list, index=index_list, columns=column_list) #type: ignore
print (dataframe)

#To print all data from column 2
print (dataframe['c2'])

#To print all data from column 2 and raw 4
print (dataframe['c2']['i4'])

#To print all data from column 3 and 4
print (dataframe[['c3','c4']])

#To select data from column 2 greater than 15
print (dataframe[dataframe['c2'] > 15])

#To return all data greater than 20 (True and False)
print (dataframe > 20)
#       c1     c2     c3     c4     c5
#i1  False  False  False  False  False
#i2  False  False  False  False  False
#i3  False  False  False  False  False
#i4  False  False  False  False  False
#i5  False   True   True   True   True

#To print data from raw 3
print (dataframe.loc['i3'])

#To select data from raw3 and column4
print (dataframe.loc['i3']['c4'])

