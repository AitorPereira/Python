#Filter data in dataframes

import pandas as pd
import numpy as np

np.random.seed(42) #We use this line to generate the same numbers along the exercise, so I can work with the same numbers
values_list = np.random.rand(10,3)
print (values_list)
# [[0.37454012 0.95071431 0.73199394]
#  [0.59865848 0.15601864 0.15599452]
#  [0.05808361 0.86617615 0.60111501]
#  [0.70807258 0.02058449 0.96990985]
#  [0.83244264 0.21233911 0.18182497]
#  [0.18340451 0.30424224 0.52475643]
#  [0.43194502 0.29122914 0.61185289]
#  [0.13949386 0.29214465 0.36636184]
#  [0.45606998 0.78517596 0.19967378]
#  [0.51423444 0.59241457 0.04645041]]

#To convert the list into a dataframe
dataframe = pd.DataFrame(values_list)
print (dataframe)
#           0         1         2
# 0  0.374540  0.950714  0.731994
# 1  0.598658  0.156019  0.155995
# 2  0.058084  0.866176  0.601115
# 3  0.708073  0.020584  0.969910
# 4  0.832443  0.212339  0.181825
# 5  0.183405  0.304242  0.524756
# 6  0.431945  0.291229  0.611853
# 7  0.139494  0.292145  0.366362
# 8  0.456070  0.785176  0.199674
# 9  0.514234  0.592415  0.046450

#To print the first column
column0 = dataframe[0]
print (column0)
# 0    0.374540
# 1    0.598658
# 2    0.058084
# 3    0.708073
# 4    0.832443
# 5    0.183405
# 6    0.431945
# 7    0.139494
# 8    0.456070
# 9    0.514234

#To sort out all data from the first column greater than 0.40
column0[column0 > 0.40]
# 1    0.598658
# 3    0.708073
# 4    0.832443
# 6    0.431945
# 8    0.456070
# 9    0.514234

#To sort out all from the dataframe greater than 0.40
print (dataframe[dataframe > 0.40])
#           0         1         2
# 0       NaN  0.950714  0.731994
# 1  0.598658       NaN       NaN
# 2       NaN  0.866176  0.601115
# 3  0.708073       NaN  0.969910
# 4  0.832443       NaN       NaN
# 5       NaN       NaN  0.524756
# 6  0.431945       NaN  0.611853
# 7       NaN       NaN       NaN
# 8  0.456070  0.785176       NaN
# 9  0.514234  0.592415       NaN

