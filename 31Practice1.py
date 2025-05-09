# Create a function 'create_full_name' that builds a person's full name,
# passing 3 parameters to the function: first_name, last_name1, and last_name2
#
# For example:
# first_name = 'Antonio'
# last_name1 = 'Rodriguez'
# last_name2 = 'Perez'
#
# The function should return: 'Antonio Rodriguez Perez'
#
# Note: Make sure to include a space between each part of the name

def create_full_name(first_name, last_name1, last_name2):
    full_name = first_name + " " + last_name1 + " " + last_name2
    return full_name