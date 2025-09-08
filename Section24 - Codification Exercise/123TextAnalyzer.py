# Create a function called analyze_text that receives a text and analyzes the words it contains,
# returning relevant information such as the frequency of each word and the average word length.
#
# The function must preserve accents and remove only punctuation marks.
#
# Instructions:
#
# The function analyze_text must receive a single parameter:
#     text: A string where the words will be analyzed.
#
# The function must process the text to:
#     - Remove only punctuation marks (such as periods, commas, question marks, etc.), 
#       while keeping accents and other special characters.
#     - Convert the entire text to lowercase so words are treated equally regardless of capitalization.
#
# The function must calculate and return a dictionary containing:
#     - Word frequency: A dictionary where keys are the words and values are the number of times 
#       each word appears in the text.
#     - Most frequent word: The word that appears most often in the text.
#     - Average word length: The average length of the words in the text (rounded to two decimals).
#
# In the case of an empty text (i.e., if no words are found), the function must return:
#     - An empty dictionary ({}) for the word frequency.
#     - An empty string ('') as the most frequent word.
#     - 0 as the average word length.

def analyze_text(text):
    if text.strip():
        special_char = '?¿!¡.,;-'
        for char in special_char:
            text = text.replace(char, '')
        text = text.lower()

        words = text.split()

        if not words:
            return {
            'Word frequency':{},
            'Most frequent word':'',
            'Average Word Length':0
            }

        word_frequency = {}
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        most_frequent_word = max(word_frequency, key=word_frequency.get)
        
        total_length=0
        for word in words:
            total_length += len(word)
        average_length = round(total_length / len(words), 2)
    
        return {
            'Word frequency':word_frequency,
            'Most frequent word':most_frequent_word,
            'Average word length':average_length
        }


# print(analyze_text("¡Hola! ¿Cómo estás? Estoy bien, bien feliz."))


# Create a function called analyze_text that receives a text and analyzes the words it contains,
# returning relevant information such as the frequency of each word and the average word length.
#
# The function must preserve accents and remove only punctuation marks.
#
# Instructions:
#
# The function analyze_text must receive a single parameter:
#     text: A string where the words will be analyzed.
#
# The function must process the text to:
#     - Remove only punctuation marks (such as periods, commas, question marks, etc.), 
#       while keeping accents and other special characters.
#     - Convert the entire text to lowercase so words are treated equally regardless of capitalization.
#
# The function must calculate and return a dictionary containing:
#     - Word frequency: A dictionary where keys are the words and values are the number of times 
#       each word appears in the text.
#     - Most frequent word: The word that appears most often in the text.
#     - Average word length: The average length of the words in the text (rounded to two decimals).
#
# In the case of an empty text (i.e., if no words are found), the function must return:
#     - An empty dictionary ({}) for the word frequency.
#     - An empty string ('') as the most frequent word.
#     - 0 as the average word length.
    

            
        
            