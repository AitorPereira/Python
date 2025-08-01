#Creating a FileText
#WriteText --> wt

file = open("creatingtextfile.txt", "wt")

file_text = "Hi, this is the first line we are going to save in our first text file."

file.write(file_text)

#we need to close the file
file.close()

