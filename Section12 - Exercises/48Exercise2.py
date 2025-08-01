# String contains numbers
# Create a function named 'contains_numbers' that checks if the string passed as a parameter contains any numbers.
# If the string has numbers, this function will return True
# Otherwise, it will return False

# Importing the 're' module to use regular expressions
# import re

# Define the function 'contains_numbers' that takes a string as a parameter
# def contains_numbers(string):
#     return bool(re.search(r'\d', string))  # Returns True if a digit is found, otherwise False

# Usage examples

# string1 = "Hello, this is a string without numbers."  # A string without any numbers
# string2 = "This string contains 123 numbers."          # A string that includes numbers

# print(contains_numbers(string1))  # Should print False
# print(contains_numbers(string2))  # Should print True

import re

def contains_numbers(string):
    list = re.split(r"\s",string)
    for word in list:
        if any(character.isdigit() for character in word):
            return True
    return False

answer = contains_numbers("The text has numbers 912")
print (answer)