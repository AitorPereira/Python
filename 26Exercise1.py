# Create a dictionary with the following key-value pairs:
#    apple, manzana
#    orange, naranja
#    banana, platano
#    lemon, limon
#Show the translation for the word "orange"  
#Add a new element with "pineapple" and "piña"  
#Create a loop to display all the elements of the dictionary

dictionary = {"apple":"manzana", "orange":"naranja", "banana":"platano", "lemon":"limon"}

print (dictionary["orange"])
dictionary.update({"pineapple":"piña"})
#for fruit in dictionary.items():
#    print (fruit)

for key, value in dictionary.items():
    print (f"The fruit {key} is {value} in spanish")