#
# Import dependencies
#

import os

from tkinter import *

from tkinter import messagebox as mb

from tkcalendar import Calendar

from datetime import datetime

import ftplib

from classes.FTP import *

#
# Config
#

class Medical_CSV_Export:

    host = "127.0.0.1"
    username = "username"
    password = "password"

    def action(self):

        # User Interface stores the user's option in a variable.
        date = calendar.selection_get()
        
        # date.year = Year user selected.
        # date.month = Month user selected.
        # date.day = Day user selected.        
        file_name = "MED_DATA_" + date.year + "0803153931"

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
            self.error( "A file does not exist for the date selected" )
            
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

        # Show a confirmation message        
        self.confirmation( "File successfully downloaded")

        # Lastly, open the file directory.
        os.startfile( destination_path )


    def main(self):
        global calendar
        
        # Create the Window.
        window = Tk()

        # Set the title of the Window.
        window.wm_title("CalendarDialog Demo")

        # Creates the Label
        label = Label(text="Hello, Tkinter")

        # Adds the Label to the Window
        label.pack()

        # Create a Calendar, that the user can choose a date on.
        # Defaults to the current day, month and year.        
        calendar = Calendar(window, selectmode = 'day',
                       year = datetime.now().year, month = datetime.now().month,
                       day = datetime.now().day)

        # Adds the Calendar to the Window        
        calendar.pack()
            
        # Define a button, on the Window, which when pressed calls the function action.
        button = Button(window, text ="Import data", command = self.action )

        # Adds the Button to the Window.
        button.pack()

        # Update the window with the elements        
        window.update()

        window.mainloop()

    def confirmation( self, message ):
         mb.showinfo( "Ok", message )

    def error( self, message ):
         mb.showerror( "Ok", message )

Medical_CSV_Export = Medical_CSV_Export()
Medical_CSV_Export.main()
