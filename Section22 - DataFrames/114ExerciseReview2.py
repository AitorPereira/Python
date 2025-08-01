import pandas as pd
import numpy as np

# def operations_with_series(series1, series2):
#     concatenation = pd.concat(series1, series2)
#     print(concatenation)


import pandas as pd
import numpy as np

def operations_with_series(series1, series2):
    dataframe = pd.DataFrame(series1)
    dataframe2 = pd.DataFrame(series2)
    concatenation = pd.concat([series1, series2])
    sum_result = dataframe + dataframe2
    average = np.mean([series1, series2])
    return {
        "concatenated_series": concatenation,
        "sum_of_values": sum_result,
        "average_of_values": average
    }