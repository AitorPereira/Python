import pandas as pd

dataframe1 = pd.DataFrame({'c1':['1','2','3'], 'key':['a','b','c']})
print (dataframe1)
#  c1 key
# 0  1   a
# 1  2   b
# 2  3   c

dataframe2 = pd.DataFrame({'c2':['4','5','6'], 'key':['c','b','e']})
print (dataframe2)
#   c1 key
# 0  1   a
# 1  2   b
# 2  3   c


#To create the union
#To assign how we want to make the union, we will use on='word' 
dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2,on='key')
print (dataframe3)
#   c1 key c2
# 0  2   b  5
# 1  3   c  4

# To merge two different DataFrames while keeping one and adding the other, we use how='left' or how='right'.
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2, on='key', how='left')
print (dataframe4)
#   c1 key   c2
# 0  1   a  NaN
# 1  2   b    5
# 2  3   c    4

dataframe5 = pd.DataFrame.merge(dataframe1,dataframe2, on='key', how='right')
print (dataframe5)
#     c1 key c2
# 0    3   c  4
# 1    2   b  5
# 2  NaN   e  6

# If we want to merge all DataFrames and show NaN for values that don't have a match
dataframe6 = pd.DataFrame.merge(dataframe1,dataframe2, on='key', how='outer')
print (dataframe6)
#     c1 key   c2
# 0    1   a  NaN
# 1    2   b    5
# 2    3   c    4
# 3  NaN   e    6

