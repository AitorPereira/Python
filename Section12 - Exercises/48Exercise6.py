# Count words in a file
# You are asked to create a function that writes to and reads from a text file,
# and indicates the number of words it contains.

# The text to be written into the file will span multiple lines
# and will be passed to the function as a parameter.


import re

count = 0

def write_and_read_file(file_name, text):

    try:
        # Open the file in write mode and write the text
        file = open(file_name, "wt")
        file.write(text)
        file.close()

        # Open the file again in read mode and read its content
        file = open(file_name, "rt")
        file_content = file.read()
        file.close()
        
        # Use regex to find all words
        count_words = re.findall(r"\w+", file_content)
        total_words = len(count_words)
        return total_words
    except:
        # Return -1 in case of any error
        return -1

file_name = "48Exercise6_my_file.txt"
text = """This is an example of text that will be written
on multiple lines in the file. Students should count
the words in this text and then read it from the file."""

total_words = write_and_read_file(file_name, text)

if total_words != -1:
    print(f'The file "{file_name}" contains {total_words} words.')
else:
    print(f'Error working with the file "{file_name}".')