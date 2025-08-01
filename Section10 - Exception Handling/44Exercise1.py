# Create the function "operator" that, given 3 numbers, divides the first number
# by the difference of the other two numbers.

#Use the created function with the numbers 5, 4, 2  
#Use the created function with the numbers 6, 3, 3

#Use the try ... except block to handle any possible error """

def operator(num1,num2,num3):
    try:
        result = num1 / (num2-num3)
        print (result)
    except ZeroDivisionError:
        print("Error: Division by Zero")
    finally:
        print("The operation has been completed")

operator(5,4,2)
operator(6,3,3)