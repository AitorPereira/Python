#Sorting series

import pandas as pd
import numpy as np

values_list = range(4)
index_list = list ('CABD')
serie = pd.Series(values_list, index=index_list)
#C    0
#A    1
#B    2
#D    3

#To sort the serie by index
serie.sort_index()
#A    1
#B    2
#C    0
#D    3

#To sort the serie by values
serie.sort_values()
#C    0
#A    1
#B    2
#D    3

#To rank all positions (fewer to greater)
serie.rank()
#C    1.0
#A    2.0
#B    3.0
#D    4.0

serie2 = pd.Series(np.random.randn(10))
print (serie2)
#0   -0.995006
#1   -1.708708
#2   -0.831656
#3    1.369298
#4   -1.194005
#5   -0.847408
#6    1.127988
#7    0.415252
#8   -1.323445
#9    0.736101
print (serie2.rank())
#0     4.0
#1     1.0
#2     6.0
#3    10.0
#4     3.0
#5     5.0
#6     9.0
#7     7.0
#8     2.0
#9     8.0
serie2.sort_index()
serie2.sort_values()