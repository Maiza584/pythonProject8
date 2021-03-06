# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()
master.title('Python Desktop Application')

# sets the geometry of main
# root window
master.geometry("400x400")


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


label = Label(master,
              text="First window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Gestures recognition",
             command=openNewWindow)
btn.pack(pady=10)



# Python code to illustrate read() mode
file = open("Practice.py", "r")
print(file.read())


# Python code to create a file
file = open('bye.xlsx','w')
file = open('hi.xlsx.py','w')
file.write("This is the write command")
file.write("I will write all data here")
file.close()


btn.pack(pady=10)
foreground = "red",  # Set the text color to white
background = "black",  # Set the background color to black

# mainloop, runs infinitely
mainloop()