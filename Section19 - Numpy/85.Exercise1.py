# Create the function “pares” that returns an array of even numbers between two values
# passed as parameters to the function (start and end).
# Use the “pares” function with the numbers 1 and 30.
# Use the “pares” function with the numbers 2 and 40.

import numpy as np

#my way
def even(start,end):
    evens = []
    array = np.arange(start,end)
    for number in array:
        if number % 2 == 0:
            evens.append(number)
    return np.array(evens)

print (even(1,30))
print (even(2,40))

#different way
def even2(start, end):
    #If the start number is even:
    if start % 2 == 0:
        array = np.arange(start,end,2)
    #If the start number is odd:
    else:
        start = start + 1
        array = np.arange(start,end,2)
    return array