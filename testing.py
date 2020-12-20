from functools import partial
from tkinter import *

ValidLogin = False


def validateLogin(username, password):
    CoveredPassword = '*' * len(password.get())
    print("username entered :", username.get())
    print("password entered :", CoveredPassword)
    if username.get() == 'Jack':
        if password.get() == 'Jack123':
            print('Valid Credentials!')
            ValidLogin = True
            if input('Would you like to see the entered password? >> ') == 'yes':
                print(password.get())
            elif input == 'Yes':
                print(password.get())
        else:
            ValidLogin = False
            exit('Invalid credentials. This incedent will be reported.')


class App:
    def __init__(self):
        self.root = Tk()
        button = Button(self.root, text='root quit', command=self.quit)
        button.pack()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()


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
