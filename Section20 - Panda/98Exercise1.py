# Exercise

# We have 3 classes: "class1", "class2", "class3"
# We are going to generate a random number of students for each class
# To get a random number we will use:
#     np.random.randint(minimum, maximum, number)

# Create a series of classes and their number of students
# Use the index of the created series to find out how many students are in class2

import pandas as pd
import numpy as np

#One way
# class1 = pd.Series(np.random.randint(0,30))
# print (class1)

# class2 = pd.Series(np.random.randint(10,30))
# print (class2)

# class3 = pd.Series(np.random.randint(10,30))
# print (class3)

minimum = 5
maximum = 30
num = 3

student_list = list(np.random.randint(minimum,maximum,num))
index_list = ['class1','class2','class3']
serie = pd.Series(student_list, index=index_list)
print (serie)

print (serie['class2'])
