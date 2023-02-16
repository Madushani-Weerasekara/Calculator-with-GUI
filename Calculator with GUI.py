
from tkinter import *# import tkinter

root_window = Tk() # create a new tkinter window using TK() class

root_window.title("Calculator") # set the title of the window

root_window.mainloop() # display the window. This loop helps to keep the window open untill the user close it or exit the program.

input_box = Entry(root_window, width=50, borderwidth=5) # create a new entry widget and store it in input_box vsriable
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #places the input_box widget inside the root window using the grid() method.

def button_click(number):

    current = input_box.get() #retrieves the current value of the calculator display widget, which is stored in the e variable.
    input_box.delete(0,END) # clear all -delete all of the text in the widget, starting from the beginning (index 0) and continuing to the end.
    input_box.insert = str(current) + str(number) # inserts the new number clicked by the user into the display widget by converting it to a string and concatenating it with the previous value stored in current.

 



