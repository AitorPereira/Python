#This is used for large text fields for example Comments field

import tkinter

root = tkinter.Tk()
root.title("My program")

insert = tkinter.Text(root)
insert.config(width=20,height=10,font=("Arial",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")
insert.pack()


root.mainloop()