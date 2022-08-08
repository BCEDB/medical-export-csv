from tkinter import *

from tkcalendar import *

class CalendarDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        self.calendar = Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection


def onclick():
    cd = CalendarDialog( window )
    print(cd.result)

# Create the Window.
window = Tk()

# Set the title of the Window.
window.wm_title("CalendarDialog Demo")

# Creates the Label
label = Label(text="Hello, Tkinter")

# Adds the Label to the Window
label.pack()
    
# Define a button, on the Window, which when pressed calls the function buttonCallBack.
Button = Button(window, text ="Show calendar", command =onclick)

# Adds the Button to the Window.
Button.pack()

window.update()

window.mainloop()

# Creates the Dropdown
#dropdown = StringVar( window )

# Set the Default Value for the Dropdown.
#dropdown.set("one")

# Sets the options on the Dropdown
#dropdown_element = OptionMenu( window, dropdown, "one", "two", "three" )

# Adds the Dropdown to the Window.
#dropdown_element.pack()

# Define a button, on the Window, which when pressed calls the function buttonCallBack.
#Button = Button(window, text ="Hello", command =buttonCallBack)

