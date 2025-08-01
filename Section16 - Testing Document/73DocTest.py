# Doctest - generate test within the documentation
#It's IMPORTANT to add a SPACE after >>> to avoid any error when commenting for launching a test
#To execute code in terminal is best to pick names with no spaces or special characters
#To execute the code, access all the way to the folder by using cd or ls in the terminal
#once found it, use this command: python3 exercisename.py -v


def addition(num1, num2):
    """
    This is the documentation of this function.
    It receives two numbers as parameters and returns its sum
    >>> addition(3,4)
    7
    >>> addition(4,6)
    10
    >>> addition (1,3)
    9
    """
    return num1 + num2

result = addition(2, 4)
print(result)

import doctest
doctest.testmod()