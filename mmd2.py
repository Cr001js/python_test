from csv import reader
from hashlib import sha256

dict = {}

count = 0

while count < 1:

    name = input('enter your name = ')

    if name == 'stop':
        count +=1
        break


    password = input('enter your password = ')


    password = sha256(password.encode('utf-8')).hexdigest()

    up_name = name
    argument = name + ',' + password
    


    with open ('rain.csv', 'a+')as f:
        f.write(argument)
        f.write('\n')
    
