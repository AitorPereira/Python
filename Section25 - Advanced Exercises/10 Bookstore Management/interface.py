from tkinter import *
import database
from tkinter import messagebox

def pulse_display():
    window_list.delete(0, END)
    books = database.display()
    for book in books:
        window_list.insert(END, book)

def pulse_search():
    window_list.delete(0, END)
    books = database.search(title.get(), author.get(), year.get(), isbn.get())
    for book in books:
        window_list.insert(END, book)

def pulse_add():
    database.add(title.get(), author.get(), year.get(), isbn.get())
    window_list.delete(0, END)
    books = database.display()
    for book in books:
        window_list.insert(END, book)

def pulse_remove():
    database.remove(selected_book[0])
    window_list.delete(0, END)
    window_list.insert(END, "Book has been succesfully removed")

def pulse_close():
    answer = messagebox.askyesno("Exit", "Are you sure you want to close the program?")
    if answer:
        messagebox.showinfo("Goodbye", "Thanks for using the program!")
        frame.quit()

def selected_row_book(event):
    try:
        global selected_book
        index = window_list.curselection()[0]
        selected_book = window_list.get(index)

        title_entry.delete(0, END)
        title_entry.insert(END, selected_book[1])

        author_entry.delete(0,END)
        author_entry.insert(END, selected_book[2])

        year_entry.delete(0,END)
        year_entry.insert(END, selected_book[3])

        isbn_entry.delete(0,END)
        isbn_entry.insert(END, selected_book[4])
    
    except IndexError:
        pass

def pulse_update():
    database.update(title.get(), author.get(), year.get(), isbn.get(), selected_book[0])
    window_list.delete(0, END)
    window_list.insert(END, "Book has been succesfully updated")

frame = Tk()

frame.title("Bookstore")


title_label = Label(frame, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(frame, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(frame, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(frame, text="Isbn")
isbn_label.grid(row=1, column=2)



title = StringVar()
title_entry = Entry(frame, textvariable=title)
title_entry.grid(row=0, column=1)

author = StringVar()
author_entry = Entry(frame, textvariable=author)
author_entry.grid(row=0, column=3)

year = StringVar()
year_entry = Entry(frame, textvariable=year)
year_entry.grid(row=1, column=1)

isbn = StringVar()
isbn_entry = Entry(frame, textvariable=isbn)
isbn_entry.grid(row=1, column=3)

window_list = Listbox(frame, bg="gray", height=8, width=25)
window_list.grid(row=2, column=0, rowspan=6, columnspan=2, padx=10)

scroll_list = Scrollbar(frame)
scroll_list.grid(row=2, column=2, rowspan=6)

window_list.configure(yscrollcommand=scroll_list.set)
scroll_list.configure(command=window_list.yview)

window_list.bind('<<ListboxSelect>>', selected_row_book)

Button(frame, text="Display", fg="gray", bg="gray", command=pulse_display, width=10, height=1).grid(row=2, column=3, padx=2, pady=2)
Button(frame, text="Search", fg="gray", bg="gray", command=pulse_search, width=10, height=1).grid(row=3, column=3, padx=2, pady=2)
Button(frame, text="Add", fg="gray", bg="gray", command=pulse_add, width=10, height=1).grid(row=4, column=3, padx=2, pady=2)
Button(frame, text="Update", fg="gray", bg="gray", command=pulse_update, width=10, height=1).grid(row=5, column=3, padx=2, pady=2)
Button(frame, text="Remove", fg="gray", bg="gray", width=10, command=pulse_remove, height=1).grid(row=6, column=3, padx=2, pady=2)
Button(frame, text="Close", fg="gray", bg="gray", width=10, command=pulse_close, height=1).grid(row=7, column=3, padx=2, pady=2)


frame.mainloop()



#To create an executable file, get into your route and run this command on your terminal:
#pyinstaller interface.py --onefile --windowed

