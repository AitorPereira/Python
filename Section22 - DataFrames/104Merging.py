import pandas as pd
import numpy as np

serie1 = pd.Series ([1,2, np.nan])
print (serie1)
# 0    1.0
# 1    2.0
# 2    NaN

serie2 = pd.Series ([4,5,6])
print (serie2)
# 0    4
# 1    5
# 2    6

# To merge two Series: if a value in the first Series is null, it takes the value from the second Series.
# Otherwise, it keeps the value from the first Series.
serie3 = serie1.combine_first(serie2)
print (serie3)
# 0    1.0
# 1    2.0
# 2    6.0

values_list = [1,2,np.nan]
dataframe1 = pd.DataFrame(values_list)
print (dataframe1)
#      0
# 0  1.0
# 1  2.0
# 2  NaN
values_list2 = [4,5,6]
dataframe2 = pd.DataFrame(values_list2)

# To merge two Dataframes: if a value in the first dataframe is null, it takes the value from the second dataframe.
# Otherwise, it keeps the value from the first dataframe.
dataframe3 = dataframe1.combine_first(dataframe2)
print (dataframe3)
#      0
# 0  1.0
# 1  2.0
# 2  6.0