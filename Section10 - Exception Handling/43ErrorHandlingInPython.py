#try - except - else - finally
try:
    num1 = 5
    num2 = 0
    division = num1/num2
    print(division)
except ZeroDivisionError:
    print("Error, division by zero")
except:
    print("There was an error")
else:
    print("The division was done correctly")
finally:
    print("This tryout has been ended")