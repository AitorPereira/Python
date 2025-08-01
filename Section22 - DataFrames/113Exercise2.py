# Exercise

# Create 2 arrays with 9 random integer numbers between 0 and 100
# Reshape the arrays into a structure of 3 rows by 3 columns
# Create 2 DataFrames from those arrays
# Concatenate the 2 DataFrames

import pandas as pd
import numpy as np

# Create 2 arrays with 9 random integer numbers between 0 and 100
array1 = np.array(np.random.randint(0,100,9))
array2 = np.array(np.random.randint(0,100,9))

# Reshape the arrays into a structure of 3 rows by 3 columns
array1 = array1.reshape(3,3)
print (array1)
array2 = array2.reshape(3,3)
print (array2)

# Create 2 DataFrames from those arrays
dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)

# Concatenate the 2 DataFrames
#To organize index correctly we will use: ignore_index=True
dataframe3 = pd.concat([dataframe1, dataframe2], ignore_index=True)
print (dataframe3)
