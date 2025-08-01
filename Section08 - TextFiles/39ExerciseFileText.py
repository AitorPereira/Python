# Create the module "39Exercise1.py"
# Create a class "File"
# Create the function "read_file" to read from a text file
# Create the function "write_file" to create a text file
# Create the function "append_file" to add data at the end of a text file

# Create a program "39ExerciseFileText.py"
# Create the object "file" from the class "File" in the module "39Exercise1.py"
# Use the method "write_file" from the object "file" to create a new text file
# Use the method "append_file" to add more data to the end of the file
# Use the method "read_file" to view all the content of the file

# Run the program "39ExerciseFileText.py" from the command terminal

import mExercise139

#we name the new txt file we are making
filename = 'textfile1.txt'
#Then we call mExercise139 module and we use '.File' because that's the class name and 'filename'. 
file = mExercise139.File(filename)

text = "This is the first line of the file. \n This is going to be the second line"

file.write_file(text)

text = "\n this is the third line"

file.append_file(text)

read_text = file.read_file()
print (read_text)
