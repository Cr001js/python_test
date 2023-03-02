from csv import reader
from hashlib import sha256
hash_pass_to_pass = {}

for password in range(1,10000):
    hashing_number = sha256(b'%i'% password).hexdigest()
    hash_pass_to_pass[hashing_number] = password

with open ('rain.csv')as f:
    password_singer = reader(f)
    for row in password_singer:
        name_users = row[0]

        for key in row [1:]:
            print(name_users,":", hash_pass_to_pass[key])


