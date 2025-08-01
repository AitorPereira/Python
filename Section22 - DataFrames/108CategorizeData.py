import pandas as pd
import numpy as np

prices = [42,55,48,23,5,21,88,34,26]
price_range = [0,10,20,30,40,50,60,70,80,90,100]

prices_with_range = pd.cut(prices, price_range)
print (prices_with_range)
# [(40, 50], (50, 60], (40, 50], (20, 30], (0, 10], (20, 30], (80, 90], (30, 40], (20, 30]]
# Categories (10, interval[int64, right]): [(0, 10] < (10, 20] < (20, 30] < (30, 40] ... (60, 70] <
#                                           (70, 80] < (80, 90] < (90, 100]]

count_prices = pd.value_counts(prices_with_range)
print (count_prices)
# (20, 30]     3
# (40, 50]     2
# (0, 10]      1
# (30, 40]     1
# (50, 60]     1
# (80, 90]     1
# (10, 20]     0
# (60, 70]     0
# (70, 80]     0
# (90, 100]    0

