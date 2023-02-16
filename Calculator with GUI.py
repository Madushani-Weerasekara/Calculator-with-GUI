 

from tkinter import *# import tkinter
import math

root_window = Tk() # create a new tkinter window using TK() class

root_window.title("Calculator") # set the title of the window


input_box = Entry(root_window, width=50, borderwidth=5) # create a new entry widget and store it in input_box vsriable
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #places the input_box widget inside the root window using the grid() method.

def button_click(number):

    current = input_box.get() #retrieves the current value of the calculator display widget, which is stored in the input_box variable.
    input_box.delete(0, END) # clear all -delete all of the text in the widget, starting from the beginning (index 0) and continuing to the end.
    input_box.insert = str(current) + str(number) # inserts the new number clicked by the user into the display widget by converting it to a string and concatenating it with the previous value stored in current.
 
 # The function to handle the clear button.
def clear():
    input_box.delete(0, END)

# Define the functions to handle the operations.
def button_addition():

    global f_num
    global math
    f_num = input_box.get() # get the entered value and store it in f_num variable
    math = "addition"
    f_num = float(f_num)
    input_box.delete(0, END)

def button_subtract():

    global f_num
    global math
    f_num = input_box.get()
    math = "subtraction"
    f_num = float(f_num)
    input_box.delete(0, END)

def button_division():

    global f_num
    global math
    f_num = input_box.get()
    math = "Devision"
    f_num = float(f_num)
    input_box.delete(0, END)

def button_multiply():

    global f_num
    global math
    f_num = input_box.get()
    math = "multiplication"
    f_num = float(f_num)
    input_box.delete(0, END)

# The functions to handle the equal button.
def buton_equal():

    
    second_num = input_box.get()
    input_box.delete(0, END)

    if math == "addition":
        input_box.insert(0, f_num + float(second_num))

    elif math == "subtraction":
        input_box.insert(0, f_num - float(second_num))

    elif math == "division" :
        input_box.insert(0, f_num / float(second_num))

    elif math == "multiplication" :
        input_box.insert(0, f_num * float(second_num))



# Add the number and operation buttons.
# Example :-when the button is clicked, the lambda function is called, which in turn calls the button_click function with the argument 1. This will update the calculator display to show the number 1.

# number buttons(0-1)
button_1 = Button(root_window, text="1",padx=40, pady=20, command=lambda: button_click(1))
button_1.grid(row=3, column=1) # place the buttons in the main window.
button_2 = Button(root_window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2.grid(row=3, column=2)
button_3 = Button(root_window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3.grid(row=3, column=3)
button_4 = Button(root_window, text="4", padx=40, pady=20, command=lambda:  button_click(4))
button_4.grid(row=2, column=1)
button_5 = Button(root_window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_5.grid(row=2, column=2)
button_6 = Button(root_window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_6.grid(row=2, column=3)
button_7 = Button(root_window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_7.grid(row=1, column=1)
button_8 = Button(root_window,text="8", padx=40, pady=20, command=lambda: button_click(8))
button_8.grid(row=1, column=2)
button_9 = Button(root_window,text="9", padx=40,pady=20,command=lambda: button_click(9))
button_9.grid(row=1, column=3)
button_0 = Button(root_window,text="0", padx=40,pady=20,command=lambda: button_click(0))
button_0.grid(row=4, column=1)

# operatin buttons
button_addition = Button(root_window, text="+", padx=39, pady=20, command=lambda: button_addition())
button_addition.grid(row=4, column=4)
button_subtract = Button(root_window, text="-", padx=39, pady=20, command=lambda: button_subtract())
button_subtract.grid(row=3, column=4)
button_division = Button(root_window, text="/", padx=39, pady=20, command=lambda: button_division())
button_division.grid(row=1, column=4)
button_multiply = Button(root_window, text="*", padx=39, pady=20, command=lambda: button_multiply())
button_multiply.grid(row=2, column=4)

button_equal = Button(root_window, text="=", padx=40, pady=20, command=lambda:button_equal())
button_multiply.grid(row=4, column=3)
button_clear = Button(root_window, text="C", padx=40, pady=20, command=lambda:button_clear())
button_multiply.grid(row=4, column=2)

root_window.mainloop() # display the window. This loop helps to keep the window open untill the user close it or exit the program.
