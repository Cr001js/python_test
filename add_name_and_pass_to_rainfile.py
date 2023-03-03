# Required modules:)
from csv import reader
from hashlib import sha256
# This code takes your name and password and saves it in rain.csv


dict = {}
count = 0

while count < 1:

    name = input('enter your name = ')

    if name == 'stop': # if you 'stop', code will stops
        count +=1
        break


    password = input('enter your password = ')


    password = sha256(password.encode('utf-8')).hexdigest()

    up_name = name
    argument = name + ',' + password
    
    with open ('other/rain.csv', 'a+')as f:
        f.write(argument)
        f.write('\n')
# code will never stops until you enter stop (ᵔᴥᵔ)