# Create a function that converts Celsius temperature to Fahrenheit temperature.

# Define the variable 'temperature_celsius' (Celsius temperature input).
# Define the variable 'temperature_fahrenheit' (Fahrenheit temperature output).

# We have already written the entire function,
# and you only need to fill in the line where we calculate the value of the variable 'temperature_fahrenheit'
# using the following formula:

# temperature_fahrenheit = (temperature_celsius * 9/5) + 32

# The rest of the code is already written.

def temp_converter(temperature_celsius):
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    return temperature_fahrenheit

print(temp_converter(10))