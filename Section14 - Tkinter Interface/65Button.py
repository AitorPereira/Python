import tkinter

root = tkinter.Tk()
root.title("My program")

#We need to define the command action before we create the button

def action():
    print("Hi World")

button = tkinter.Button(root, text="Execute", command=action)
button.config(fg="green")
button.pack()

root.mainloop()