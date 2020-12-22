from functools import partial
from tkinter import *

ValidLogin = False


def validateLogin(username, password):
    CoveredPassword = '*' * len(password.get())
    print("username entered :", username.get())
    print("password entered :", CoveredPassword)
    if username.get() == 'a':
        if password.get() == 'a':
            print('Valid Credentials!')
            global ValidLogin  # Makes it usable everywhere in the code, so that they understand when Login = Successful
            ValidLogin = True
            tkWindow.destroy()
            if input('Would you like to see the entered password? >> ') == 'yes':
                print(password.get())
            elif input == 'Yes':
                print(password.get())
    else:
        ValidLogin = False
        exit('Invalid credentials. This incident will be reported.')


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login')

# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
# Phase 2 -------------------------------------------------------------------------------------------------------------

fileconfig = False

# TODO: Try using strip(), `==` operators, Dict(), set(), list(), tuple(),

# Define all the possible user input commands:
def userCommand(userInput):
    if userInput.get() == 'openfile':
        global fileconfig
        fileconfig = True
    else:
        pass


# Set new window dimensions
phaseTwoWindow = Tk()
phaseTwoWindow.geometry('400x150')
phaseTwoWindow.title('Tkinter Login')

# Set the code entry label and text box configuration
shellLabel = Label(phaseTwoWindow, text="Shell Command >> ").grid(row=0, column=0)
userInput = StringVar()
codeEntry = Entry(phaseTwoWindow, textvariable=shellLabel).grid(row=0, column=1)
submit = Button(phaseTwoWindow, text="Submit to Console", command=userCommand(userInput)).grid(row=4, column=1)


# Open File Window
openfileWindow = Tk()
openfileWindow.geometry('400x150')
openfileWindow.title('Open File Config')

# Close window button
closeWindow = Button(openfileWindow, text='X', command=openfileWindow.destroy)
closeWindow.pack()

if ValidLogin:
    phaseTwoWindow.mainloop()

while fileconfig:
    openfileWindow.mainloop()
else:
    openfileWindow.destroy()
