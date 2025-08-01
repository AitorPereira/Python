# Exercise
# Create an array with 100 random integers with values between 0 and 500
# Use a box plot to represent the generated random values

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

list1 = np.random.randint (0,501,100)
array_list = pd.Series(list1)
sns.boxplot(array_list)
plt.title("Boxplot of 100 Random Integers between 0 and 500")
plt.show()