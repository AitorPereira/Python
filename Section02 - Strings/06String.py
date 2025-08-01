string = "Hello World"

# H e l l o  W o r l d
# 0 1 2 3 4 5 6 7 8 9

#To print a specific character in the string
print (string[6])

#To print a specific range of characters in the string
print (string[0:5])

#To print the string from a specific character to the end
print (string[6:])

#To print the string from the start to a specific character
print (string[:5])

#To print the string in reverse
print (string[::-1])

#We can check what's found in that position but we can't replace. This is an ERROR:
string[5] = "p"


