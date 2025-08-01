#PopOut Question Yes or No

import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("My program")

def ask():
    result = messagebox.askquestion("Question Title","Do you want to delete this file?")
    if result == "yes":
        print("Yes, I want to delete the file")
    else:
        print("No, I do not want to delete the file")


button = tkinter.Button(root, text="Click to ask", command=ask)
button.pack()

root.mainloop()