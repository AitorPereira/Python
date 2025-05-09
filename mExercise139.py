# Create the module "39Exercise1.py"
# Create a class "File"
# Create the function "read_file" to read from a text file
# Create the function "write_file" to create a text file
# Create the function "append_file" to add data at the end of a text file

# Create a program "program1.py"
# Create the object "file" from the class "File" in the module "39Exercise1.py"
# Use the method "write_file" from the object "file" to create a new text file
# Use the method "append_file" to add more data to the end of the file
# Use the method "read_file" to view all the content of the file

# Run the program "program1.py" from the command terminal

class File:
    def __init__(self,filename):
        self.filename = filename

    def write_file(self, text):
        data = open (self.filename, "wt")
        data.write(text)
        data.close()

    def append_file(self, text):
        data = open (self.filename, "at")
        data.write(text)
        data.close()

    def read_file(self):
        data = open(self.filename, "rt")
        text = data.read()
        return text