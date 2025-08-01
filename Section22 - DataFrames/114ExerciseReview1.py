# Basic statistics
# Let's create a function that calculates basic statistics (mean, median, and standard deviation)
# from a list of numbers passed as a parameter.

# def calculate_statistics(data):
#     # Function implementation goes here
#     pass

# # Example of use
# data = [10, 20, 30, 40, 50]

# statistics = calculate_statistics(data)
# print("Statistics:")
# print("Mean:", statistics["mean"])
# print("Median:", statistics["median"])
# print("Standard Deviation:", statistics["standard_deviation"])

# Output:
# Statistics:
# Mean: 30.0
# Median: 30.0
# Standard Deviation: 14.142135623730951
import pandas as pd
import numpy as np

data = [10, 20, 30, 40, 50]

def calculate_statistics(data):
    if not data:
        return None
    serie = pd.Series(data)
    return {
        "Media": serie.mean(),
        "Mediana": serie.median(),
        "Desviacion Estandar": serie.std(ddof=0)
    }

print(calculate_statistics([10, 20, 30, 40, 50]))

