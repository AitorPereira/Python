#Create a function named create_json that receives 3 input parameters: name, age, and city,
#and returns a JSON structure with the input data.

# Example of use

#name = "John"
#age = 25
#city = "Sampleville"

#json_result = create_json(name, age, city)
#print(json_result)

import json
def create_json(name, age, city):
    example_json = {"name":name,"age":age,"city":city}
    json_structure = json.dumps(example_json)
    return json_structure

json_final = create_json("John",25,"Sampleville")
print(json_final)
