import tkinter
#from tkinter import font
#to know what fonts do you have installed use: from tkinter import font

root = tkinter.Tk()
root.title("My Program")

#Label Creation
text = "Hi World"

label = tkinter.Label(root,text=text)
label.config(fg="green", bg="lightgrey", font=("Arial", 30),)
label.pack()

#and then use: print(font.families())
#print(font.families())

root.mainloop()
