#Remove duplicates in dataframes

import pandas as pd

values_list = [[1,2], [1,2], [5,6], [5,8]]
print (values_list)

index_list = list('mnop')
print (index_list)
# ['m', 'n', 'o', 'p']

columns_list = ['value1','value2']

dataframe = pd.DataFrame(values_list, index=index_list, columns=columns_list)
print (dataframe)
#    value1  value2
# m       1       2
# n       1       2
# o       5       6
# p       5       8

#if we want to remove the raws that has duplicate items
dataframe_remove_raws = dataframe.drop_duplicates()
print (dataframe_remove_raws)
#    value1  value2
# m       1       2
# o       5       6
# p       5       8

#If we want to remove the columns with duplicate items
dataframe_remove_columns = dataframe.drop_duplicates(['value1'])

#To keep the last item in case that there's duplicates, we need to add keep='last'
dataframe_remove_columns = dataframe.drop_duplicates(['value1'], keep='last')
