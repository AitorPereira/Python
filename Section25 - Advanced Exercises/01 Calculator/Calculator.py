# 📟 Calculator using Tkinter
# Supports basic operations, square root, power, decimal, AC, and backspace

import tkinter
from simpleeval import simple_eval, SimpleEval
import math

# --- Setup Root Window ---
root = tkinter.Tk()
root.title("Calculator")

# --- Main Frame ---
frame = tkinter.Frame(root, bg="gray", width=400, height=1200)
frame.pack()
frame.pack_propagate(False)  # Prevent frame from resizing

# --- Entry Field (Screen) ---
insert = tkinter.Entry(frame, justify="center", width=32)
insert.grid(row=1, column=0, columnspan=5, pady=4)


# --- Functional Logic ---

def result():
    """Evaluate the expression and display the result."""
    expression = insert.get()

    # Auto-close open parentheses
    open_parens = expression.count('(')
    close_parens = expression.count(')')
    if open_parens > close_parens:
        expression += ')' * (open_parens - close_parens)

    try:
        s = SimpleEval()
        s.functions["sqrt"] = math.sqrt  # Add sqrt support
        result = s.eval(expression)

        insert.delete(0, tkinter.END)
        insert.insert(tkinter.END, str(result))

    except:
        insert.delete(0, tkinter.END)
        insert.insert(tkinter.END, 'Error')

def pulse_ac():
    """Clear the input field."""
    insert.delete(0, tkinter.END)

def pulse_remove():
    """Remove last character."""
    current = insert.get()
    insert.delete(0, tkinter.END)
    insert.insert(tkinter.END, current[:-1])


# --- Number Buttons ---

def pulse0(): insert.insert(tkinter.END, '0')
def pulse1(): insert.insert(tkinter.END, '1')
def pulse2(): insert.insert(tkinter.END, '2')
def pulse3(): insert.insert(tkinter.END, '3')
def pulse4(): insert.insert(tkinter.END, '4')
def pulse5(): insert.insert(tkinter.END, '5')
def pulse6(): insert.insert(tkinter.END, '6')
def pulse7(): insert.insert(tkinter.END, '7')
def pulse8(): insert.insert(tkinter.END, '8')
def pulse9(): insert.insert(tkinter.END, '9')


# --- Operator Buttons ---

def pulse_add(): insert.insert(tkinter.END, '+')
def pulse_sub(): insert.insert(tkinter.END, '-')
def pulse_mul(): insert.insert(tkinter.END, '*')
def pulse_div(): insert.insert(tkinter.END, '/')
def pulse_dot(): insert.insert(tkinter.END, '.')
def pulse_power(): insert.insert(tkinter.END, '**')

def pulse_squareroot():
    insert.insert(tkinter.END, 'sqrt(')

# --- Buttons Grid Layout ---

# Row 2
tkinter.Button(frame, text="**", fg="green", command=pulse_power, width=4, height=2).grid(row=2, column=0)
tkinter.Button(frame, text="√", fg="green", command=pulse_squareroot, width=4, height=2).grid(row=2, column=1)
tkinter.Button(frame, text="AC", fg="green", command=pulse_ac, width=4, height=2).grid(row=2, column=2)
tkinter.Button(frame, text="←", fg="green", command=pulse_remove, width=4, height=2).grid(row=2, column=3)

# Row 3
tkinter.Button(frame, text="1", fg="green", command=pulse1, width=4, height=2).grid(row=3, column=0, padx=5, pady=5)
tkinter.Button(frame, text="2", fg="green", command=pulse2, width=4, height=2).grid(row=3, column=1, padx=5, pady=5)
tkinter.Button(frame, text="3", fg="green", command=pulse3, width=4, height=2).grid(row=3, column=2, padx=5, pady=5)
tkinter.Button(frame, text="4", fg="green", command=pulse4, width=4, height=2).grid(row=3, column=3, padx=5, pady=5)

# Row 4
tkinter.Button(frame, text="5", fg="green", command=pulse5, width=4, height=2).grid(row=4, column=0, padx=5, pady=5)
tkinter.Button(frame, text="6", fg="green", command=pulse6, width=4, height=2).grid(row=4, column=1, padx=5, pady=5)
tkinter.Button(frame, text="7", fg="green", command=pulse7, width=4, height=2).grid(row=4, column=2, padx=5, pady=5)
tkinter.Button(frame, text="8", fg="green", command=pulse8, width=4, height=2).grid(row=4, column=3, padx=5, pady=5)

# Row 5
tkinter.Button(frame, text="9", fg="green", command=pulse9, width=4, height=2).grid(row=5, column=0, padx=5, pady=5)
tkinter.Button(frame, text="0", fg="green", command=pulse0, width=4, height=2).grid(row=5, column=1, padx=5, pady=5)
tkinter.Button(frame, text=".", fg="green", command=pulse_dot, width=4, height=2).grid(row=5, column=2, padx=5, pady=5)
tkinter.Button(frame, text="+", fg="green", command=pulse_add, width=4, height=2).grid(row=5, column=3, padx=5, pady=5)

# Row 6
tkinter.Button(frame, text="-", fg="green", command=pulse_sub, width=4, height=2).grid(row=6, column=0, padx=5, pady=5)
tkinter.Button(frame, text="*", fg="green", command=pulse_mul, width=4, height=2).grid(row=6, column=1, padx=5, pady=5)
tkinter.Button(frame, text="/", fg="green", command=pulse_div, width=4, height=2).grid(row=6, column=2, padx=5, pady=5)
tkinter.Button(frame, text="=", fg="green", command=result, width=4, height=2).grid(row=6, column=3, padx=5, pady=5)


# --- Start GUI ---
root.mainloop()
