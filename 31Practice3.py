#Given an array of integers called numbers,
#create a function in Python that returns True if all the elements in the array are unique
#and False if there is any repeated element in the array.

def elementos_distintos(numbers):
    if len(numbers) == len(set(numbers)):
        return True 
    else:
        return False
