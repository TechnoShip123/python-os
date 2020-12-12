#! usr/bin/env Python

username = 'Jack'


def openfile(file):
    f = open(file, 'r')
    return f.read()


Uprompt = username + ' >> '  # Define the user prompt (Uprompt) for Jack and Kelsy. 'name >> '

if 'openfile' in (input(Uprompt)):
    Userinput = input('What file would you like to input? >> ')
    print(openfile(Userinput))
