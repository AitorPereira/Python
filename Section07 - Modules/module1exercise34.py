# Exercise

# Create a module called "module1.py"
# Add the class "Car" created in a previous exercise to the module "module1"
# Add the lambda function "average" created in a previous exercise to the module "module1"

# Create a Python program called "program1.py"
# Import the module "module1" created earlier
# Create an object "car1" by instantiating the class "Car"
# Use print to display the characteristics of the car
# Calculate the average of 3 grades and print the result

# Run the program "program1.py" and observe the output

class Car:
    def __init__(self,brand,color,engine,fuel_size):
        self.brand = brand
        self.color = color
        self.engine = engine
        self.fuel_size = fuel_size


def lambdamodule(grade1,grade2,grade3):
    average = lambda grade1, grade2, grade3 : (grade1 + grade2 + grade3)/3
    print (average(grade1,grade2,grade3))