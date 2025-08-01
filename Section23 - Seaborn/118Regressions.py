# Regressions. It is a statistical process for estimating the relationships between variables.
# It helps to understand how the value of one variable changes based on the values of other variables.
# Linear regression is a mathematical model used to approximate the dependency relationship between variables.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

sns.lmplot(x='total_bill', y='tip',data=tips, scatter_kws={'color':'green'},line_kws={'color':'blue'}) #scatter_kws = circles % line_kws = line
plt.show()

sns.lmplot(x='total_bill', y='tip',data=tips, fit_reg=False) #Fit_reg=False to remove the line
plt.show()

#To create a new column in our dataset for the percentage of the tip based on total_bill then:
tips['percentage'] = 100 * tips ['tip'] / tips['total_bill']
print (tips.head())

sns.lmplot(x='size',y='percentage',data=tips)
plt.show()

#To define and separate men and women
sns.lmplot(x='total_bill',y='percentage',data=tips, hue='sex', markers=['x','o'])
plt.show()

#To define and separate the day of the week
sns.lmplot(x='total_bill',y='percentage',data=tips, hue='day')
plt.show()

