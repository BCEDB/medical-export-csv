#
# Import dependencies
#

from tkinter import *
import ftplib

#
# Config
#

host = "127.0.0.1"
port = 21
username = "username"
password = "password"
download_path = ""

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

file_name = "MED_DATA_2022080315931"

#
# FTP
#

# Establish FTP connection
 
ftp = ftplib.FTP( host )
ftp.login( username, password )

# Check file exists on the FTP Server.
try:
    resp = ftp.sendcmd( ( "MLST " + file_name + ".csv" ) )
except:
    # File does not exist, error handling.
    print("Error. The file specified does not exist on the server.")

# File does exist, proceed.
if 'type=file;' in resp:
    with open( download_path + file_name + ".csv", 'wb') as f:
        ftp.retrbinary('RETR ' + file_name + ".csv", f.write)
 
ftp.quit()

#
# Data Validation
#

# Validate the file.
# Name validation has already occured.

# Lastly, open the file directory.
