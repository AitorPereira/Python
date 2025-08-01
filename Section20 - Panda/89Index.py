import pandas as pd
value_list = [1,2,3]
index_list=['a','b','c']

serie = pd.Series(value_list,index=index_list)
print (serie)

#This will print index
print(serie.index)

#You are allow to print index but not changes them
#serie.index[4] = 'z'

print (serie.index[2])


value_list2 = [[3,4,5],[6,8,9],[9,5,6]]
index_list2 = ['biology','astronomy','algebra']
name_list = ['John','Arthur','Anna']

dataframe = pd.DataFrame(value_list2, index=index_list2, columns=name_list) # type: ignore
print (dataframe)

#to print index
print (dataframe.index)

#to print value

print (dataframe.index[1])