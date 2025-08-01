# Box Plot
# It is used to graphically represent a series of numerical data through their quartiles.
# In this way, it shows the median (50% of the values) and the other 25% on the left and right

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1 = np.random.rand(100)
sns.boxplot(data1)
plt.show()