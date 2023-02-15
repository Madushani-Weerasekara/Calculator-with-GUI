from tkinter import *# import tkinter

root = Tk() # create a new tkinter window using TK() class

root.title("Calculator") # set the title of the window

root.mainloop() # display the window. This loop helps to keep the window open untill the user close it or exit the program.

input_box = Entry(root, width=50, borderwidth=5) # create a new entry widget and store it in input_box vsriable
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #places the input_box widget inside the root window using the grid() method.




