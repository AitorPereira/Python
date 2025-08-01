import tkinter

root = tkinter.Tk()
root.title("My program")

def verify():
    value = check1.get()
    if value is 1:
        print("Check is enable")
    else:
        print ("Check is disabled")

check1 = tkinter.IntVar()

checkbutton = tkinter.Checkbutton(root, text="Option1", variable=check1, onvalue=1, offvalue=0, command=verify)
checkbutton.pack()

root.mainloop()