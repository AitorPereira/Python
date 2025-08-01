#Word Count
#Define a function that receives a sentence as a parameter and returns the number of times
#each word appears in the text

#text = "This is a sample word count. This is a simple exercise."
#result = count_words(text)
#print(f'result = {result}')

# Expected output:
#result = {'this': 2, 'is': 2, 'a': 2, 'sample': 1, 'word': 1, 'count': 1, 'simple': 1, 'exercise': 1}

import re

def word_counter(text):
    dic_words = {}
    split_words = re.findall(r"\w+",text.lower())
    for word in split_words:
        if word in dic_words:
            dic_words[word] += 1
        else:
            dic_words[word] = 1
    return dic_words

text = "This is a sample word count. This is a simple exercise."
result = word_counter(text)
print (f'result = {result}')
