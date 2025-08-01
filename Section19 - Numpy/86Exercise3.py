# Exercise

# Create a list with the numeric values from 0 to 30
# Create another list with the first 10 values from the initial list
# Create another list with the last 10 values from the initial list
# Create a loop that goes through this last list of final values

import numpy as np

list1 = np.arange(0, 30)

first_ten = list1[0:10]
print (first_ten)

third_ten = list1[-10:]
print (third_ten)

for n in third_ten:
    print (n)

