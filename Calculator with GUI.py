
from tkinter import *# import tkinter
import math

root_window = Tk() # create a new tkinter window using TK() class

root_window.title("Calculator") # set the title of the window

root_window.mainloop() # display the window. This loop helps to keep the window open untill the user close it or exit the program.

input_box = Entry(root_window, width=50, borderwidth=5) # create a new entry widget and store it in input_box vsriable
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #places the input_box widget inside the root window using the grid() method.

def button_click(number):

    current = input_box.get() #retrieves the current value of the calculator display widget, which is stored in the input_box variable.
    input_box.delete(0, END) # clear all -delete all of the text in the widget, starting from the beginning (index 0) and continuing to the end.
    input_box.insert = str(current) + str(number) # inserts the new number clicked by the user into the display widget by converting it to a string and concatenating it with the previous value stored in current.
 
 # The function to handle the clear button.
def clear():
    input_box.delete(0, END)

# The functions to handle the equal button.
def buton_equals():

    f_num = input_box.get()
    second_num = input_box.get()
    input_box.delete(0, END)

    if math == "addition":
        input_box.insert(0, f_num + int(second_num))

    if math == "substraction":
        input_box.insert(0, f_num - int(second_num))

    if math == "Devition" :
        input_box.insert(0, f_num / int(second_num))

    if math == "multiplication" :
        input_box.insert(0, f_num * int(second_num))

# Add the number and operation buttons.
# Example :-when the button is clicked, the lambda function is called, which in turn calls the button_click function with the argument 1. This will update the calculator display to show the number 1.

# number buttons(0-1)
button_1 = Button(root_window, text="1",padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root_window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root_window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root_window, text="4", padx=40, pady=20, command=lambda:  button_click(4))
button_5 = Button(root_window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root_window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root_window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root_window,text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root_window,text="9", padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root_window,text="0", padx=40,pady=20,command=lambda: button_click(0))

# operatin buttons
button_add = Button(root_window, text="+", padx=39, pady=20, command=lambda: button_add())
button_substract = Button(root_window, text="-", padx=39, pady=20, command=lambda: button_substract())
button_devide = Button(root_window, text="/", padx=39, pady=20, command=lambda: button_devide())
button_multiply = Button(root_window, text="*", padx=39, pady=20, command=lambda: button_multiply())

button_equal = Button(root_window, text="=", padx=40, pady=20, command=lambda:button_equal())
button_clear = Button(root_window, text="C", padx=40, pady=20, command=lambda:button_clear())