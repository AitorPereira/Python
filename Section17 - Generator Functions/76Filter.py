# The filter function filters elements from a list based on a conditional function.
# The result is a new list containing only the elements that meet the condition.

def positive (num):
    """
    This function will return only positive numbers.
    """
    if (num > 0):
        return True
    else:
        return False

result = positive(-3)
print (result)

numbers = [4, -2, 8, -3, -5, -7, 1, 9]

#Filter can generate a new list from another list as you can see, printing only positive numbers

filter = filter(positive, numbers)
result = list(filter)
print(result)