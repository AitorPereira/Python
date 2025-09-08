# Calculate the number of paint cans needed to paint a wall  
# We will ask the user for:
#
# Height of the wall  
# Width of the wall  
# How many square meters one paint can covers  
#
# We will create a function that calculates the number of cans  
# Formula = (Height * Width) / m2 covered by each can

import math

print("Hi there! Welcome to your favorite tool for painters!\nWe'll make your life easier!")
print("Please enter accurate measurements for better results:")
height = int(input("What is the height of the wall to paint (meters): "))
width = int(input("What is the width of the wall to paint (meters): "))
paint_per_bucket = int(input("How many meters can one paint bucket cover: "))


def math_paint_function(height,width,paint_per_bucket):
    number_of_cans_needed = (height*width)/paint_per_bucket
    number_of_cans_needed_rounded = math.ceil(number_of_cans_needed)
    return f"You will need a total of {number_of_cans_needed_rounded} buckets to paint that wall.\nThank you for using this tool one more time."


print(math_paint_function(height,width,paint_per_bucket))