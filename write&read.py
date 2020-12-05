username = 'Jack'


def openfile():
    f = open('file.txt', 'r')  # It will open file.txt
    print(f.read())  # It will print what it reads from file.txt
    f.close()  # It will close file.txt


if username == 'Jack':
    userinput = input('Jack >> ')

# noinspection PyUnboundLocalVariable
if userinput == 'openfile':
    openfile()
else:
    print('Error, invalid command')

#  TODO: Add multiple files that are readable using a single 'openfile' and the parameter (filename) which is dependent.
