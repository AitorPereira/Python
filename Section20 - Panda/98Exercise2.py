# Exercise

# Given the Excel file provided to you in various formats
# Copy the data to the clipboard
# Create a DataFrame called "data" using the copied data
# Display all the data in the DataFrame
# Show all the column names of the DataFrame
# Show the first row of the DataFrame
# Show the first column of the DataFrame
# Show all rows but only the columns "Continent" and "Population"
# Show the first 3 rows of the DataFrame
# Show the last 2 rows of the DataFrame

import pandas as pd
import numpy as np

#Data copied from CSVfile
data_continents = pd.read_clipboard()
data = pd.DataFrame(data_continents)
#Display all the data
print (data)
#Show all the columns names
print(data.columns)
#Show the first row
print(data.loc[0])
#Show the first column
print(data['Continente'])
# #Show all rows but only the columns "Continent" and "Population"
print(data[['Continente','Población']])
#Show the first 3 rows
print (data.head(3))
#Show the last 2 rows
print (data.tail(2))

