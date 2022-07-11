# Simple Calculator program
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL

root = tkinter.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0,0)


# Colors and fonts defintion
#dark_green = "#93af22"
dark_green = "#478978"
peach = "#a37774"
white_green = "#edefe0"
button_font = ("Arial", 18)
display_font = ("Arial", 30)

# Function definitions
def submit_number(number):
    '''Add a number or decimal to display'''
    display.insert(END, number)

    # Avoid user from inserting more than one decimal point
    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    '''Store the first number of the expression and operation to be used'''
    global first_number
    global operation

    operation = operator
    first_number = display.get()

    display.delete(0, END)
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    decimal_button.config(state=NORMAL)

def equal():
    '''Run the operation'''
    if operation == "add":
        value = float(first_number) + float(display.get())
    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    elif operation == "multiply":
        value = float(first_number) * float(display.get())
    elif operation == "divide":
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == "exponent":
        value = float(first_number) ** float(display.get())

    display.delete(0, END)
    display.insert(0, value)

    enable_buttons()


def enable_buttons():
    '''Enable buttons for further calculations'''
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    decimal_button.config(state=NORMAL)


def clear():
    '''Clear the display'''
    display.delete(0, END)
    enable_buttons()


def inverse():
    '''Inverse calculation'''
    if display.get() == "0":
        value = "ERROR"
    else:
        value = 1 / float(display.get())

    display.delete(0, END)
    display.insert(0, value)


def square():
    '''Square calculation'''
    value = float(display.get())**2

    display.delete(0, END)
    display.insert(0, value)


def negate():
    '''Negate the given number'''
    value = -1 * float(display.get())

    display.delete(0, END)
    display.insert(0, value)


# GUI Layout
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

# Display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

# Button frame
clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=dark_green, command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=dark_green, command=root.destroy)

# Operator buttons
inverse_button = tkinter.Button(button_frame, text="1/x", font=button_font, bg=peach, command=inverse)
square_button = tkinter.Button(button_frame, text="x^2", font=button_font, bg=peach, command=square)
exponent_button = tkinter.Button(button_frame, text="x^n", font=button_font, bg=peach, command=lambda:operate("exponent"))
divide_button = tkinter.Button(button_frame, text=" / ", font=button_font, bg=peach, command=lambda:operate("divide"))
multiply_button = tkinter.Button(button_frame, text=" * ", font=button_font, bg=peach, command=lambda:operate("multiply"))
subtract_button = tkinter.Button(button_frame, text=" - ", font=button_font, bg=peach, command=lambda:operate("subtract"))
add_button = tkinter.Button(button_frame, text=" + ", font=button_font, bg=peach, command=lambda:operate("add"))
equal_button = tkinter.Button(button_frame, text=" = ", font=button_font, bg=dark_green, command=equal)
decimal_button = tkinter.Button(button_frame, text=" . ", font=button_font, bg="black", fg="white", command=lambda:submit_number("."))
negate_button = tkinter.Button(button_frame, text="+/- ", font=button_font, bg="black", fg="white", command=negate)

# Number buttons
nine_button = tkinter.Button(button_frame, text="9", font=button_font, bg="black", fg="white", command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text="8", font=button_font, bg="black", fg="white", command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text="7", font=button_font, bg="black", fg="white", command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text="6", font=button_font, bg="black", fg="white", command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text="5", font=button_font, bg="black", fg="white", command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text="4", font=button_font, bg="black", fg="white", command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text="3", font=button_font, bg="black", fg="white", command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text="2", font=button_font, bg="black", fg="white", command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text="1", font=button_font, bg="black", fg="white", command=lambda:submit_number(1))
zero_button = tkinter.Button(button_frame, text="0", font=button_font, bg="black", fg="white", command=lambda:submit_number(0))

# Layout buttons onto screen
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="we")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="we")

inverse_button.grid(row=1, column=0, pady=1, sticky="we")
square_button.grid(row=1, column=1, pady=1, sticky="we")
exponent_button.grid(row=1, column=2, pady=1, sticky="we")
divide_button.grid(row=1, column=3, pady=1, sticky="we")

seven_button.grid(row=2, column=0, pady=1, sticky="we", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="we", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="we", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="we", ipadx=20)

four_button.grid(row=3, column=0, pady=1, sticky="we")
five_button.grid(row=3, column=1, pady=1, sticky="we")
six_button.grid(row=3, column=2, pady=1, sticky="we")
subtract_button.grid(row=3, column=3, pady=1, sticky="we")

one_button.grid(row=4, column=0, pady=1, sticky="we")
two_button.grid(row=4, column=1, pady=1, sticky="we")
three_button.grid(row=4, column=2, pady=1, sticky="we")
add_button.grid(row=4, column=3, pady=1, sticky="we")

negate_button.grid(row=5, column=0, pady=1, sticky="we")
zero_button.grid(row=5, column=1, pady=1, sticky="we")
decimal_button.grid(row=5, column=2, pady=1, sticky="we")
equal_button.grid(row=5, column=3, pady=1, sticky="we")


root.mainloop()
