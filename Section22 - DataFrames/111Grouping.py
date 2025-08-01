#Grouping in dataframes

import pandas as pd
import numpy as np

np.random.seed(30)
values_list = {'key1':['x','x','y','y','z'], 'key2':['a','b','a','b','a'], 'data1':np.random.rand(5), 'data2':np.random.rand(5)}
print (values_list)
# {'key1': ['x', 'x', 'y', 'y', 'z'], 
# 'key2': ['a', 'b', 'a', 'b', 'a'], 
# 'data1': array([0.64414354, 0.38074849, 0.66304791, 0.16365073, 0.96260781]), 
# 'data2': array([0.34666184, 0.99175099, 0.2350579 , 0.58569427, 0.4066901 ])}

dataframe = pd.DataFrame(values_list)
print (dataframe)
#   key1 key2     data1     data2
# 0    x    a  0.644144  0.346662
# 1    x    b  0.380748  0.991751
# 2    y    a  0.663048  0.235058
# 3    y    b  0.163651  0.585694
# 4    z    a  0.962608  0.406690

#From the column 'data1' I want to group it by the information found in 'key1'
group1 = dataframe['data1'].groupby(dataframe['key1'])
print(group1)
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x106596c90>

#This will return the mean between x values in data1 ()
print (group1.mean())
# x    0.512446
# y    0.413349
# z    0.962608
