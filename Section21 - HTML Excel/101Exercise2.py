# Exercise
# Get the table of countries from the page 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
# Clean the data as needed so that the column names are correct

import pandas as pd
import webbrowser

url='https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
dataframe = pd.read_html(url)
dataframe = dataframe[0]
dataframe = dataframe.drop('Ubicación', axis=1)
print(dataframe)







