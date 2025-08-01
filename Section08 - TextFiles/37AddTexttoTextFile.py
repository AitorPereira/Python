#We need to open the textfile we want to add text to. 
#append text ---> Append Text
#\n for jumping into the next line, it's like an enter

file = open("35TextFiles.txt", "at")

text_file = "\nThis is the third line of the text"

file.write(text_file)

file.close
