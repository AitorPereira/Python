# Let's filter data in a DataFrame

# We will create a list of 50 random integer values between 0 and 100
# We will create a list of 50 random integer values between 0 and 100
# We will filter the DataFrame to display only the values greater than 50

import pandas as pd
import numpy as np

# We will create a list of 50 random integer values between 0 and 100
values_list = np.random.randint(0,100,50)
print (values_list)

# We will create a list of 50 random integer values between 0 and 100
dataframe = pd.DataFrame(values_list.reshape(5,10))
print (dataframe)

# We will filter the DataFrame to display only the values greater than 50
print (dataframe[dataframe>50])