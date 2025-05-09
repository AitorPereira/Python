# Create a function 'sum_elements' that will receive a list of numbers as an argument
# and return the sum of all the elements in the list.

def sum_elements(number_list):
    total = 0
    for num in number_list:
        total = num + total
    return total