# Example:
# Create a list of 1000 random values that follow a normal distribution
# Create a histogram using matplotlib with the list of values
# Create a box plot (where 50% of the values are concentrated) using seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

list1 = np.random.randn(1000)

plt.hist(list1)
plt.show()

sns.boxplot(list1)
plt.show()