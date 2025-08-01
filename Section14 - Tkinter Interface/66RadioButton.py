import tkinter

root = tkinter.Tk()
root.title("My program")

def select():
    print("The selected option is {}".format(option.get()))
option= tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(root, text="Option 1", variable=option, value=1, command=select)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(root, text="Option 2", variable=option, value=2, command=select)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(root, text="Option 3", variable=option, value=3, command=select)
radiobutton3.pack()


root.mainloop()