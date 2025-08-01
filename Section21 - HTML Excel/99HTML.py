#HTML in Python

import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url) #type: ignore
# print(dataframe)

dataframe_soccer = dataframe[0]
print (dataframe_soccer)

#if we need to replace the columns name
#dict(dataframe_soccer.loc[0])
#dataframe_soccer = dataframe_soccer.rename(columns=dict(dataframe_futbol.loc[0]))
#dataframe_soccer = dataframe.soccer.drop(0)

#To remove a column we need to indicate by using axis=1
dataframe_soccer = dataframe_soccer.drop('Notas',axis=1)
print (dataframe_soccer)