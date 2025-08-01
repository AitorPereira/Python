# Create a function "search" that uses a regular expression to check if a word is in a sentence

# Test the "search" function with these phrases
#text = "This is a test sentence to perform searches"
#word_to_search = 'sentence'

# If the word is found in the sentence, indicate the starting and ending position
import re

def search(word, sentence):
    find_word = re.search(word,sentence)
    return find_word

word = "sentence"
sentence = "This is a test sentence to perform searches"

search = search(word,sentence)

if (search):
    print ("Word '{}' has been founded".format(word))
    start_position = search.start()
    end_position = search.end()
    print("The word '{}' begins in the position {} and end in the position {}".format(word,start_position,end_position))
else:
    print("Word '{}' has NOT been founded".format(word))


