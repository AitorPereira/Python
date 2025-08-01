#Regular Expressions (search, findall, split, hub)
import re

text = "Hi, my name is Aitor"

find_word = re.search("name",text)
print(find_word)

word2 = re.search ("adios",text)

if (find_word):
    print("String founded")
else:
    print("Not Founded")

#We can use the dollar sign $ to find a word for the end
word3 = re.search ("Aitor$",text)
#We can use caret ^ to find a word for the beginning
word4 = re.search ("^Hi",text)
#We can use the dot and the asterisk to find words between them
word5 = re.search ("my.*is",text)
print(word5)

#findall is used to find all the words that match the pattern

text2 = """
Luis's car is a red one
Antonio's car is white
and Maria's car is blue
"""

#We can use the findall method to find all the words that match the pattern
cars = re.findall("car",text2)
print(cars)

#We can use split method to split the text into a list
textsplit = "The chair is white and cost 80 dollars"
text4 = re.split("\s",textsplit)
print(text4)

#We can use the sub method to replace the words that match the pattern
text = re.sub("car","bike",text2)
print(text)

