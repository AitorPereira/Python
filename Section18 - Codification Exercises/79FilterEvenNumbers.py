# Filter Even Numbers  

# Create a function that checks if a number is even or not

# Create another function that filters the even numbers from a list of numbers


# Example of use
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = filter_evens(numbers)
# print("Even numbers:", even_numbers)

def is_even(n):
    return n % 2 == 0 

def filter_number(numbers):
    even_list = filter(is_even, numbers)
    return list(even_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_number(numbers)
print (result)





