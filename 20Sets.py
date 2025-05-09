#Sets are unordered and unindexed. They are mutable.

colors = {"red", "blue", "green"}
print (colors)

for color in colors:
    print (color)

#We can't access items in a set by referring to an index or a key.

#print (colors[0])
print (len(colors))

colors.add("yellow")
print (colors)

colors.remove("blue")
print (colors)

