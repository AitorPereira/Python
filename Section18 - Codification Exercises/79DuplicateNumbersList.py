# Duplicate numbers from a list:

# Write a function that duplicates a number passed as a parameter.

# Write another function that receives a list of numbers as a parameter
# and returns a list with the duplicated numbers.

# def duplicate(number):

# def duplicate_list(numbers):

# Example of use
# numbers = [1, 2, 3, 4, 5]

# duplicated_numbers = duplicate_list(numbers)
# print("Duplicated list:", duplicated_numbers)

def duplicate(number):
    return number * 2

def duplicate_list(numbers):
    duplicates = []
    for n in numbers:
        duplicates.append(duplicate(n))
    return duplicates

numbers = [1, 2, 3, 4, 5]
print (duplicate_list(numbers))
