#Create popup

import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("My program")

def alert():
    messagebox.showinfo("Title","Message with information")

button = tkinter.Button(root, text="Click for Alert", command=alert)
button.pack()

root.mainloop()
