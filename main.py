import logging

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

Uinput = input('Username >> ')
if Uinput not in username:
    logging.error('Attempted login with invalid USERNAME')
    exit('Invalid username. This incident will be reported.')

Pinput = input('Password >> ')
if Pinput != password[Uinput]:
    logging.error('Attempted login with invalid PASSWORD')
    exit('Incorrect password. This incident will be reported.')

print('Valid credentials. Welcome to the system! :D')
