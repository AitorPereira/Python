# Exercise

# Read the attached file "poblacion.xlsx" and load the data into a DataFrame
# Using that data, find out which is the most populated city in America

# Read the attached file "poblacion.csv" and load the data into a DataFrame
# Using that data, find out which is the most populated city in Africa

import pandas as pd

excel_file = pd.ExcelFile('/Users/aitor/Downloads/poblacion.xlsx')
dataframe = excel_file.parse('Hoja 1')
print (dataframe)
populated_city = dataframe['Ciudad más poblada'][3] #type: ignore
print (f"\f The most populated city in America is {populated_city}")

csv_file = pd.read_csv('/Users/aitor/Downloads/poblacion.csv')
dataframe = pd.DataFrame(csv_file)
print (dataframe)
print ("\f The most populated city in Africa is: {}".format(dataframe['Ciudad más poblada'][1]))



