 

import tkinter as tk # import tkinter
import math

root_window = tk.Tk() # create a new tkinter window using TK() class

root_window.minsize(width=300, height=400)

root_window.title("Calculator") # set the title of the window

# Give weight to the row and column

root_window.columnconfigure(0, weight=1)
root_window.rowconfigure(0, weight=1)

# Create a frame to hold the input widget

frame = tk.Frame(root_window)
frame.grid(row=0, column=0, sticky="nsew")


input_box = tk.Entry(root_window, width=10, borderwidth=10) # create a new entry widget and store it in input_box vsriable
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew') #places the input_box widget inside the root window using the grid() method.
# sticky = "ew" means 

def button_click(number):

    current = input_box.get() #retrieves the current value of the calculator display widget, which is stored in the input_box variable.
    input_box.delete(0, tk.END) # clear all -delete all of the text in the widget, starting from the beginning (index 0) and continuing to the end.
    input_box.insert (str(current) + str(number)) # inserts the new number clicked by the user into the display widget by converting it to a string and concatenating it with the previous value stored in current.
 
 # The function
 #  to handle the clear button.
def clear():

    input_box.delete(0, tk.END)

def clear_lastEntry(entry):
    return entry(-1)


# Define the functions to handle the operations.
def button_addition():

    global f_num
    global math
    f_num = input_box.get() # get the entered value and store it in f_num variable
    math = "addition"
    f_num = float(f_num)
    input_box.delete(0, tk.END)

def button_subtract():

    global f_num
    global math
    f_num = input_box.get()
    math = "subtraction"
    f_num = float(f_num)
    input_box.delete(0, tk.END)

def button_division():

    global f_num
    global math
    f_num = input_box.get()
    math = "division"
    f_num = float(f_num)
    input_box.delete(0, tk.END)

def button_multiply():

    global f_num
    global math
    f_num = input_box.get()
    math = "multiplication"
    f_num = float(f_num)
    input_box.delete(0, tk.END)

def button_signChange(current_value):

    # If the current value is possitive change it to negative.
    if current_value > 0:
        return -current_value

    # If the current value is negative change it to possitive. 
    elif current_value < 0:
        return current_value
    # If the current value is Zero, return zero.
    else:
        return 0

def button_percentage(num,percentage):
# return the percentage of a given number.
    return (num * percentage) / 100

def button_squareRoot(num):
# Returns the square root of a given number.
    return math.sqrt(num)

#Calculate Exponentiation
def button_square(num):
    return num ** 2

def button_cube(num):
    return num **3

def button_recip(num):
    return 1/num
# backspace
def button_back (current_value):
# Removes the last character from the given string and returns the result.
    if len(current_value )> 0:
        return current_value [:-1]

    else:
        return current_value

# Memory functions
memory_value = 0 # Initialize the memory value to zero.

def button_MC():
# clear the current value.
    global memory_value
    memory_value = 0
   

def button_MS(current_value):
# store the current value in the memory.
    global memory_value
    memory_value =current_value

def button_MR():
# returns the current memory value.
    return memory_value

def button_M_add(current_value):
# adds the current value to the memory value.
    global memory_value
    memory_value += current_value

def button_M_subtract(current_value):
# Subtracts the current value from the memory value.
    global memory_value
    memory_value -= current_value

# The functions to handle the equal button.
def button_equal():

    
    second_num = input_box.get()
    input_box.delete(0, tk.END)

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

button_1 = tk.Button(root_window, text="1",padx=40, pady=20, command=lambda: button_click(1))
button_1.grid(row=5, column=2) # place the buttons in the main window.

button_2 = tk.Button(root_window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2.grid(row=5, column=3)

button_3 = tk.Button(root_window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3.grid(row=5, column=4)

button_4 = tk.Button(root_window, text="4", padx=40, pady=20, command=lambda:  button_click(4))
button_4.grid(row=4, column=2)  

button_5 = tk.Button(root_window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_5.grid(row=4, column=3)

button_6 = tk.Button(root_window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_6.grid(row=4, column=4)

button_7 = tk.Button(root_window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_7.grid(row=3, column=2)  

button_8 = tk.Button(root_window,text="8", padx=40, pady=20, command=lambda: button_click(8))
button_8.grid(row=3, column=3)

button_9 = tk.Button(root_window,text="9", padx=40,pady=20, command=lambda: button_click(9))
button_9.grid(row=3, column=4)

button_0 = tk.Button(root_window,text="0", padx=40,pady=20,command=lambda: button_click(0))
button_0.grid(row=6, column=3)

button_decimal = tk.Button(root_window,text=".", padx=40,pady=20,command=lambda: button_click())
button_decimal.grid(row=6, column=4)



# operatin buttons
button_addition = tk.Button(root_window, text="+", padx=40, pady=20, command=lambda: button_addition())
button_addition.grid(row=5, column=5)

button_subtract = tk.Button(root_window, text="-", padx=40, pady=20, command=lambda: button_subtract())
button_subtract.grid(row=4, column=5) 

button_division = tk.Button(root_window, text="/", padx=40, pady=20, command=lambda: button_division())
button_division.grid(row=2, column=5)

button_multiply = tk.Button(root_window, text="*", padx=40, pady=20, command=lambda: button_multiply())
button_multiply.grid(row=3, column=5)

button_equal = tk.Button(root_window, text="=", padx=40, pady=20, command=lambda:button_equal())
button_equal.grid(row=6, column=5)

# Clear
button_clear_lastEntry = tk.Button(root_window, text="CE", padx=40, pady=20, command=lambda:button_clear_lastEntry())
button_clear_lastEntry.grid(row=2, column=2)

button_clear = tk.Button(root_window, text="C", padx=40, pady=20, command=lambda:button_clear())
button_clear.grid(row=2, column=3)

# +/-
button_signChange = tk.Button(root_window, text="+/-", padx=40, pady=20, command=lambda:button_clear())
button_signChange.grid(row=6, column=2)

# %
button_percentage = tk.Button(root_window,text="%", padx=40,pady=20,command=lambda: button_click())
button_percentage.grid(row=2, column=1)

# √
button_squareRoot = tk.Button(root_window, text="√", padx=40, pady=20, command=lambda:button_clear())
button_squareRoot.grid(row=3, column=1)

# Exponentiation
button_square = tk.Button(root_window, text="x^2", padx=40, pady=20, command=lambda:button_square())
button_square.grid(row=4, column=1)

button_cube = tk.Button(root_window, text="X^3", padx=40, pady=20, command=lambda:button_cube())
button_cube.grid(row=5, column=1)

#  reciprocal 
button_recip = tk.Button(root_window, text="1/x", padx=40, pady=20, command=lambda:button_recip())
button_recip.grid(row=6, column=1)

# Backspace (Delete)

button_back = tk.Button(root_window, text="×", padx=40, pady=20, command=lambda:button_back())
button_back.grid(row=2, column=4)

# Memory functions

button_M_add = tk.Button(root_window, text="M+", padx=20, pady=10, command=lambda:button_M_add())
button_M_add.grid(row=1, column=3)

button_M_subtract = tk.Button(root_window, text="M-", padx=20, pady=10, command=lambda:button_M_subtract())
button_M_subtract.grid(row=1, column=4)

button_MR = tk.Button(root_window, text="MR", padx=20, pady=10, command=lambda:button_MR())
button_MR.grid(row=1, column=2)

button_MS = tk.Button(root_window, text="MS", padx=20, pady=10, command=lambda:button_MS())
button_MS.grid(row=1, column=5)

button_MC = tk.Button(root_window, text="MC", padx=20, pady=10, command=lambda:button_MC())
button_MC.grid(row=1, column=1)
 

root_window.mainloop() # display the window. This loop helps to keep the window open untill the user close it or exit the program.
