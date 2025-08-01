#Write to a File
#Write a function that receives the name of the text file
#and the text we want to write as parameters.
#This function will return True if it successfully writes the text to the file.

def txt_file_creation(name,text):
    try:
        file = open (name+".txt", "wt")
        file.write(text)
        file.close()
        return True
    except:
        return False
    
    
name = input("Insert the name of the TXT file: ") 
text = input("Insert the information for the TXT File: ")
txt_file_creation(name,text)

