# Exercise

# From the list "numbers" which contains numbers from 1 to 10,
# obtain a new list with all items increased by 10

numbers = list(range(1,11))

def increase(n):
    return n + 10
    
# Both ways are applicable
# Logical:
mapping = map(increase,numbers)
result = list(mapping)
print (result)

#Optimized:
result_list = list(map(increase,numbers))
print (result_list)