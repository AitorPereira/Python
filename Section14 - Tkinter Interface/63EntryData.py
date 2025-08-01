#Entry is a short text that is used to describe the entry.

import tkinter

root = tkinter.Tk()
root.title("My program")

#Create a new entry component (insert data)

insert = tkinter.Entry(root)
#If we write down: show="*" inside config, it will transform every character in *, perfect for passwords
insert.config(justify="center")
insert.pack()

root.mainloop()
