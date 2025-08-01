# Seaborn is a Python library or module for creating statistical graphics in Python. 
# It is built on top of the matplotlib module and is integrated with the pandas data structure.
# Lib: https://seaborn.pydata.org/index.html

# A histogram is a graphical representation of a variable or dataset in the form of bars, 
# where the area of each bar is proportional to the frequency of the represented values.
# Set matplotlib to display plots inline (equivalent to %matplotlib inline)
#mpl.use('Agg')  # Use non-interactive backend for scripts
#mpl.ion()  # Turn on interactive mode

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1 = np.random.randn(100)
print(data1)

plt.clf()  # Clear figure


plt.hist(data1, color="gray", alpha=0.5) #alpha is to adjust intensity, the lower the lighter
# For displaying plots in Cursor/regular Python scripts
plt.show()  # This displays the plot

#For display bar graphic with line kde=True
sns.histplot(data1, kde=True, color="green")
plt.show()

data2 = np.random.randn(80)
plt.hist(data2, color="yellow", alpha=0.4)
plt.show()

#To combine both graphics

plt.hist(data1, color="green", alpha=0.3, bins=20, density=True)
plt.hist(data2, color="blue", alpha=0.3, bins=20, density=True)
plt.show()

data3 = np.random.randn(1000)
data4 = np.random.randn(1000)
sns.jointplot(x=data3, y=data4, kind="hex")
plt.show()