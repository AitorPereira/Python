#Map - Apply a function to all elements from a list

def multiply (num):
    """
    This function will return all numbers multiply by 2
    """
    return num*2

numbers = [2,4,6]

#Through "map" you can use a function to all elements from a list
#In this case, it will multiply by 2 all numbers from the list
mapping = map(multiply, numbers)

#Then we will transform the result in a list using "list(mapping)"
result = list(mapping)
print(result)

#To optimize this code, we can do it in a single line:

result_list = list(map(multiply,numbers))
print(result_list)

#Now, if we don't want to define the function like before: "def multiply", we can use a lambda function

result_list = list(map(lambda num: num*2, numbers))
print (result_list)