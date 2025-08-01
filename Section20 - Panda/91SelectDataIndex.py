#Selecting data in series

import pandas as pd
import numpy as np

values_list = np.arange(3)
index_list = ['i1','i2','i3']

serie = pd.Series(values_list, index=index_list)
print (serie)

#We can multiply our serie
serie = serie * 2
print (serie)

#Selecting our index will show the value
print (serie['i2'])
#2

print (serie[2])
#4

print (serie[0:3])
#i1    0
#i2    2

print (serie['i1':'i3'])
#i1    0
#i2    2
#i3    4

print (serie[serie > 3])
#i3    4

#To modify any parameter higher than 3
serie[serie > 3] = 6
print (serie)