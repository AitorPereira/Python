# Generate even numbers
# The task is to create a function that receives two numbers as parameters:
# 'start' and 'end', representing the beginning and end of a range.
# The function should return the even numbers within that range.

# Function definition:
# def generate_evens(start, end):
#     return [num for num in range(start, end + 1) if num % 2 == 0]

# Example usage:
# Define the start and end of the range
# start = 1
# end = 10

# Print the even numbers within the range
# print(f"Even numbers in the

def even(start,end):
    for n in range(start,end+1):
        if n % 2 == 0:
            print (n)

start = 1
end = 10
result = even(start,end)
