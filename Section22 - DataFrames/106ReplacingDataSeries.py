import pandas as pd

serie1 = pd.Series([1,2,3,4,5], index=list('abcde'))
print (serie1)
# a    1
# b    2
# c    3
# d    4
# e    5

#To replace data in a serie
serie1 = serie1.replace(1,6)
print (serie1)
# a    6
# b    2
# c    3
# d    4
# e    5

serie1 = serie1.replace({2:8,3:9})
print (serie1)
# a    6
# b    8
# c    9
# d    4
# e    5



