# Lambda Functions  
# You are asked to write a single function called 'filter_evens' that receives a list of numbers as a parameter  
# and returns a list of even numbers.

# It is required to use a lambda function to check whether a number is even or not.


# Example of use
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = filter_evens(numbers)
# print("Even numbers:", even_numbers)

def filter_evens(numbers_list):
    return list(filter(lambda n: n % 2 == 0, numbers_list))

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (filter_evens(numbers_list))