#
# Import dependencies
#

import os

from tkinter import *

from tkinter import messagebox as mb

from tkcalendar import Calendar

from datetime import datetime

import ftplib

import csv

from data_validation import *

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
        file_name = "MED_DATA_" + format(date.year, '02') + format(date.month, '02') + format(date.day, '02')
        file_name = 'MED_DATA_20220803155901.csv'

        #
        # FTP
        #
        # Establish an FTP connection
        # host: The host of the server
        # username: The username of the server
        # password: the password to connect to the FTP server
        destination_path = "./MED_DATA"
        try:
            ftp = FTP( self.host, self.username, self.password )
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

        except ConnectionRefusedError:
            print( "ERROR: FTP connection refused" )

        #
        # Data Validation
        #

        # Validate the file.
        # Name validation has already occured.

        # Read contents of file
        print("Validating file:", file_name)

        data = read_csv(path.join(destination_path, file_name))
        header = data[0]
        batch_id = data[1][0]

        # Validate the file headers
        error = ""
        valid_file = is_valid_header(file_name, header)

        if not valid_file:
            error = "Incorrect headers"
        else:

            # List all the downloaded files available
            files = [f for f in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, f))]

            # Define a dictionary to store all batch ids
            batch_ids = {}

            # Iterate through available files to check for duplicate batch id
            for file in files:
                # Skip file if its the current one
                if file == file_name:
                    continue

                # Obtain batch id from the file
                file_data = read_csv(path.join(destination_path, file))
                bid = file_data[1][0]

                # Add batch id and filename to the dictionary
                batch_ids[bid] = file

            # Validate batch_id
            if batch_id in batch_ids:
                print(batch_id)
                valid_file = False

                # Add the error message to the log
                log_error(["ERROR", file, f"Invalid batch_id '{bid}'", f"Duplicate of {batch_ids[bid]}"])
                error = "Duplicate batch ID"

        # Inform user if the file is valid
        if valid_file:
            self.confirmation( "Validation successful" )
        else:
            self.error(f"Invalid file: {error}")



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
