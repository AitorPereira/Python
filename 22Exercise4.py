#Create a variable named "dictionary" with the following key-value pairs:
#   key=uno     value=one  
#   key=dos     value=two  
#   key=tres   value=three
# Display on screen the value of the variable "dictionary".
# Add a new element to the dictionary:  
# key=cuatro   value=four
#Now display the value of the dictionary.
#Capture a value entered by keyboard and store it in "data".
#Use "data" as the key of the dictionary to retrieve its value.

dictionary = {"uno":"one", "dos":"two", "tres":"three"}
print (dictionary)

dictionary.update({"cuatro":"four"})
print (dictionary)

data = input ("Write a number: ")

value = dictionary[data]
print (value)