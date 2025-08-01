#Dataframes

import pandas as pd

import webbrowser
website = 'https://en.wikipedia.org/wiki/List_of_NBA_champions'
webbrowser.open(website)

#To select a list from a website, we will import webbrowser, add the website link, and open it
#Then we will copy a list from the website and define it in a variable

dataframe_nba = pd.read_clipboard()
print (dataframe_nba)

#To print columns name
print (dataframe_nba.columns)

#To print data from a column
print (dataframe_nba['Western'])

#To print position index 5 data
print (dataframe_nba.loc[5])

#To print the first 5 raws
print (dataframe_nba.head(5))

#To print the last 4 raws
print (dataframe_nba.tail(4))

#To create a dataframe from a dictionary
subject_grades = [6,4,7,8]
subject_names = ['history','science','chemistry','technology']
diccionary_grades = {'Grades':subject_grades,'Subject':subject_names}

dataframe_grades = pd.Series(diccionary_grades)
print (dataframe_grades)