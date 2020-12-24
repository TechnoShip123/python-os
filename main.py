#! bin/var/env Python
from tkinter import *
from betterPrint import bcolors
import time
import logging
import os

# Designing window for registration
# Self Notes: The current background color is teal

loginsuccess = False
Uinput = type(str)
logging.basicConfig(filename='incidents.log', filemode='a', level=logging.WARN, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="teal").pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username * ")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="teal", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            logging.error('Attempted login with invalid PASSWORD')
            password_not_recognised()

    else:
        logging.error('Attempted login with invalid USERNAME')
        user_not_found()


# Designing popup for login success

def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    main_screen.destroy()
    global loginsuccess
    loginsuccess = True


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="teal", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()

# PHASE TWO -----------------------------------------------------------------------------------------------------------
# noinspection PyUnboundLocalVariable
current_usr = username1


def openfile(file):
    f = open(file, 'r')
    return f.read()


# Help Command. REMEMBER TO UPDATE WHEN ADDING NEW COMMANDS

# Open File command (`openfile`)
while loginsuccess is True:
    Uinput = input(current_usr + '>> ')
    if 'openfile' in Uinput:
        user_file_input = input('What file would you like to input? >> ')
        print(openfile(user_file_input))
    elif 'exit' in Uinput:  # Exit Command
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}Logging Out...{bcolors.ENDC}")
        exit()
    elif 'help' in Uinput:  # Help Command, maybe make it open a help file instead?
        print(f"{bcolors.OKCYAN}{bcolors.BOLD}This a list of available commands:\n{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}help{bcolors.ENDC}", ' - This function lists available commands.')
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}openfile{bcolors.ENDC}", ' - This command opens a file stored in the same folder, just type in the file name at the next '
                                                                        'prompt with the file extension, for example,', f"{bcolors.OKBLUE}{bcolors.UNDERLINE}file.txt{bcolors.ENDC}")
        print('')
    else:
        print(f"{bcolors.FAIL}{bcolors.BOLD}Error: Invalid Command.{bcolors.ENDC}")
