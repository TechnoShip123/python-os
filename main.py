#! usr/bin/env Python
import logging
def openfile(file):
    f = open(file, 'r')
    return f.read()


username = [
    'Jack',
    'Kelsy',
    'username3'
]
password = {
    'Jack': 'Jack123',
    'Kelsy': 'Kelsy123',
    'username3': 'password3',
}
logging.basicConfig(filename='incidents.log', filemode='a', level=logging.WARN, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

selected_user = input('Username >> ')
if selected_user not in username:
    logging.error('Attempted login with invalid USERNAME')
    exit('Invalid username. This incident will be reported.')


Pinput = input('Password >> ')
if Pinput != password[selected_user]:
    logging.error('Attempted login with invalid PASSWORD')
    exit('Incorrect password. This incident will be reported.')

print('Valid credentials.', selected_user, 'is now logged in!')

# LOGIN COMPLETED -----------------------------------------------------------------------------------------------------

Uprompt = selected_user + ' >> '  # Define the user prompt (Uprompt) for Jack and Kelsy. 'name >> '

if 'openfile' in (input(Uprompt)):
    user_file_input = input('What file would you like to input? >> ')
    print(openfile(user_file_input))
