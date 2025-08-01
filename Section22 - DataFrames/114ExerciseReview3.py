import pandas as pd
import numpy as np

def analizar_datos_dataframe():
    nombre = ['Alice','Bob','Charlie','David','Eva']
    edad = [25,30,35,40,45]
    puntuacion = [85,92,78,88,95]
    
    dataframe = pd.DataFrame({'Nombre':nombre, 'Edad':edad, 'Puntuacion':puntuacion})
    print (dataframe)
    media = dataframe['Edad'].mean()
    return {'media_edad':media}

analizar_datos_dataframe()