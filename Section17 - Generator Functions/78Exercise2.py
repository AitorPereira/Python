# Exercise

# From the list "numbers" which contains numbers from 1 to 10,
# use "filter" to obtain a list called "evens" with the even numbers from the "numbers" list

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

numbers = list (range(1,11))

filter = filter(even,numbers)
result = list(filter)
print (result)