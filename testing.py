#! usr/bin/env Python
def openfile(file):
    f = open(file, 'r')
    return f.read()


def writefile(filename):
    w = open(filename, 'w')
    return f.read()


username = [
    'Jack',
    'Kelsy',
    'username3'
]

selected_user = input('Username >> ')
if selected_user not in username:
    # logging.error('Attempted login with invalid USERNAME')
    exit('Invalid username. This incident will be reported.')

Uprompt = selected_user + ' >> '  # Define the user prompt (Uprompt) for Jack and Kelsy. 'name >> '

if 'openfile' in (input(Uprompt)):
    user_file_input = input('What file would you like to input? >> ')
    print(openfile(user_file_input))
