#
# Import dependencies
#

import os
from tkinter import *
import ftplib
from classes.FTP import *

#
# Config
#

host = "127.0.0.1"
username = "username"
password = "password"

#
# User Interface (UI)
# Requirements: The User Interface should ask the user to select a date in a 6-month range either side of the current date.
# Additionally it should default to today's date.

# window = Tk()

# window.title("Date Selection")

# window.geometry('1000x600')
# window.configure(bg='aqua')

# lbl = Label(window, text="Day")
# lbl.grid(column=0, row=0)
# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# var =IntVar()
# var.set(3)
# spin = Spinbox(window, from_=1, to=31, width=5, textvariable=var)
# spin.grid(column=10,row=0)

# lbl = Label(window, text="Month")
# lbl.grid(column=0, row=20)
# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# var =IntVar()
# var.set(8)
# spin = Spinbox(window, from_=1, to=12, width=5, textvariable=var)
# spin.grid(column=10,row=20)

# lbl = Label(window, text="Year")
# lbl.grid(column=0, row=40)
# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# var =IntVar()
# var.set(2022)
# spin = Spinbox(window, from_=2020, to=2023, width=5, textvariable=var)
# spin.grid(column=10,row=40)

# window.mainloop()

# User Interface stores the user's option in a variable.

file_name = "MED_DATA_20220803153931"

#
# FTP
#

# Establish an FTP connection
# host: The host of the server
# username: The username of the server
# password: the password to connect to the FTP server
ftp = FTP( host, username, password )

try:
    # Download the file
    destination_path = ftp.download( file_name, "C:/" )
except FileNotFoundError as error:

    # File does not exist.
    # Close the FTP connection.
    ftp.close()

    # End the program's execution
    exit()

# Close the FTP connection
ftp.close()

#
# Data Validation
#

# Validate the file.
# Name validation has already occured.

# Lastly, open the file directory.
os.startfile( destination_path )