#Dictionaries are unordered, changeable and indexed. They are written with curly braces.
#Key and Value
color_diccionary = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}

print (color_diccionary ["red"])

valor = color_diccionary ["yellow"]
print (valor)

#to add colors to the diccionary
color_diccionary ["black"] = "negro"
print (color_diccionary)

#Pop is a function to remove one item from a diccionary.
color_diccionary.pop("yellow")
print(color_diccionary)

#Another way to delete an item would be
del(color_diccionary["black"])
print (color_diccionary)

for color in color_diccionary:
    print (color)

for clave,valor in color_diccionary.items():
    print (clave,valor)
