#Combining styles

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn._stats import density

data1 = np.random.randn(100)

""" sns.histplot(data1, color="green") #To obtain bars graphic
plt.show()

sns.kdeplot(data1, color="green") # To obtain a line graphic instead of bars graphic
plt.show() """

#To combine bars and lines separately with different parameters and a legend:
sns.histplot(data1, bins=25, color="gray", label="Histogram", stat="density") #stat = density to use the same scale for the line and bars
sns.kdeplot(data1, color="black", label="Curve")
plt.legend() #plt.legend to create a legend
plt.show()

serie1 = pd.Series(data1)
print (serie1)
sns.histplot(serie1, bins=25, color="green", kde=True)
plt.show()





