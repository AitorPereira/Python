#Aggregation (Aggregation operations that return a single value, like the mean)

import pandas as pd
import numpy as np

values_list = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]
print (values_list)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [nan, nan, nan]]

column_list = list('abc')
dataframe = pd.DataFrame(values_list, columns=column_list)
print (dataframe)
#      a    b    c
# 0  1.0  2.0  3.0
# 1  4.0  5.0  6.0
# 2  7.0  8.0  9.0
# 3  NaN  NaN  NaN

# This will sum all data from columns a, b, and c. It will also show the minimum value in all columns
# It will ignore any null information
print (dataframe.agg(['sum','min']))
#         a     b     c
# sum  12.0  15.0  18.0
# min   1.0   2.0   3.0

#This will sum all data from raws
print (dataframe.agg('sum',axis=1))
# 0     6.0
# 1    15.0
# 2    24.0
# 3     0.0
