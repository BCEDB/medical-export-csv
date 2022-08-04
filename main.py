#
# Import dependencies
#
from tkinter import *

#
# User Interface (UI)
# Requirements: The User Interface should ask the user to select a date in a 6-month range either side of the current date.
# Additionally it should default to today's date.

window = Tk()

window.title("Date Selection")

window.geometry('1000x600')
window.configure(bg='aqua')

lbl = Label(window, text="Day")
lbl.grid(column=0, row=0)
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
var =IntVar()
var.set(3)
spin = Spinbox(window, from_=1, to=31, width=5, textvariable=var)
spin.grid(column=10,row=0)

lbl = Label(window, text="Month")
lbl.grid(column=0, row=20)
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
var =IntVar()
var.set(8)
spin = Spinbox(window, from_=1, to=12, width=5, textvariable=var)
spin.grid(column=10,row=20)

lbl = Label(window, text="Year")
lbl.grid(column=0, row=40)
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
var =IntVar()
var.set(2022)
spin = Spinbox(window, from_=2020, to=2023, width=5, textvariable=var)
spin.grid(column=10,row=40)

window.mainloop()

# User Interface stores the user's option in a variable.

# User's option is translated into the file's name.

#
# FTP
#

# Establish FTP connection

# Check file exists on the FTP Server.
# File does not exist, error handling.
# File does exist, proceed.

# Download the file.

#
# Data Validation
#

# Validate the file.
# Name validation has already occured.

# Lastly, open the file directory.
