#Create a dictionary called "fruits"
#fruits = {"manzana":"apple", "banana":"banana", "naranja":"orange", "lemon":"limon"}

#Record this structure called fruits in a binary file called "file.pckl"
#since in a filetext only characters can be stored, but we can't store this structure in a text file

#recover this file structure from file.pckl
#and verify that is still being a dictionary executing the method .values()

import pickle

fruits = {"manzana":"apple", "banana":"banana", "naranja":"orange", "lemon":"limon"}

file = open("file.pckl","wb")

pickle.dump(fruits, file)

file.close()

file2 = open("Section09 - Binary Files/file.pckl","rb")

read_file_color = pickle.load(file2)

print (read_file_color)