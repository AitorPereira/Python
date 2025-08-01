#Combining elements

import pandas as pd
import numpy as np

values_list = np.arange(25).reshape(5,5)
print (values_list)
dataframe = pd.DataFrame(values_list)
random_combination = np.random.permutation(5) # To generate random numbers from 0 to 5 in different positions
print (random_combination)
# [2 1 3 0 4]

#Now to print my dataframe in the same order as the random_combination:
random_dataframe = dataframe.take(random_combination)
print (random_dataframe)