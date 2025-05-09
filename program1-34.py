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


from module1exercise34 import Car
from module1exercise34 import lambdamodule

car1 = Car("opel","black","2.0","gasoline")
print (f"My car is a {car1.brand}, in {car1.color} color, with a {car1.engine} engine and {car1.fuel_size}")

lambdamodule(8,4,5)