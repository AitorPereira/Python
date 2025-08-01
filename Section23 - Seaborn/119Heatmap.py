# A heatmap is a graphical representation of data where individual values contained in a matrix are represented with colors.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
flights.head()
#    year month  passengers
# 0  1949   Jan         112
# 1  1949   Feb         118
# 2  1949   Mar         132
# 3  1949   Apr         129
# 4  1949   May         121

flights = flights.pivot(index='month',columns='year',values='passengers')
print (flights)
# year   1949  1950  1951  1952  1953  1954  1955  1956  1957  1958  1959  1960
# month                                                                        
# Jan     112   115   145   171   196   204   242   284   315   340   360   417
# Feb     118   126   150   180   196   188   233   277   301   318   342   391
# Mar     132   141   178   193   236   235   267   317   356   362   406   419
# Apr     129   135   163   181   235   227   269   313   348   348   396   461
# May     121   125   172   183   229   234   270   318   355   363   420   472
# Jun     135   149   178   218   243   264   315   374   422   435   472   535
# Jul     148   170   199   230   264   302   364   413   465   491   548   622
# Aug     148   170   199   242   272   293   347   405   467   505   559   606
# Sep     136   158   184   209   237   259   312   355   404   404   463   508
# Oct     119   133   162   191   211   229   274   306   347   359   407   461
# Nov     104   114   146   172   180   203   237   271   305   310   362   390
# Dec     118   140   166   194   201   229   278   306   336   337   405   432

sns.heatmap(flights, annot=True, fmt='d') #Annot=True & fmt='d' for annotations
plt.show()

#To select a specific parameter
middle_value = flights.loc['May'][1956]
#318

#To add a center value:
sns.heatmap(flights, center=middle_value, annot=True, fmt='d')
plt.show()

#To move the color line legend from the right side to the bottom
sns.heatmap(flights, center=middle_value, annot=True, fmt='d', cbar_kws={'orientation':'horizontal'})
plt.show()

