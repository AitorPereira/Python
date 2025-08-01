#Lists are ordered, changeable and allow duplicate values.

colors = ["red", "blue", "yellow", "purple"]

print (colors[0])

#To replace a color from the list
colors[0] = "black"
print (colors)

#Len to check the size of hte list
print (len(colors))

#.Append to add
colors.append ("pink")
print (colors)

#To remove an item from the list
colors.remove ("yellow")
print (colors)

#to print all colors from a list 
for color in colors:
    print (color)

#to remove all colors
colors.clear()
print (colors)

colors.index