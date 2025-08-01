#JSON is a format for storing and exchanging data that is in text format.

#Convert data from a dictionary Python to a JSON string

product1 ={"name":"chair","color":"white","cost":100}
import json

json_structure = json.dumps(product1)
print(json_structure)

#Can't find the key or value because JSON storage information in a text format.
#However we do can find the position of any character in the string by using the index.
print(json_structure[0])

#Now we will convert back a JSON string to a dictionary Python

product2 =json.loads(json_structure)
print(product2)

#now we can access to the value of the key of the dictionary
print(product2["name"])