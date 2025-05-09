# Validate sum
# Create a function in Python that adds 3 numbers and checks if the sum is greater or less than 100
# If the sum is greater than 100, the function will return the text "The sum is greater than 100"
# If the sum is less than 100, the function will return the text "The sum is less than 100"

def validate_sum_100(number1, number2, number3):
    total = number1 + number2 + number3
    if total > 100:
        result = "The sum is greater than 100"
    else:
        result = "The sum is less than 100"

    return result
