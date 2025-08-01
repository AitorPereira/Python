#filedialog to open a file

import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.title("My program")

def openfile():
    filepath = filedialog.askopenfilename(title="Open file")
    print (filepath)

button = tkinter.Button(root,text="Click for start",command=openfile)
button.pack()

root.mainloop()