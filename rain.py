# Required modules:)
from csv import reader
from hashlib import sha256
# this code find's passwords of amir, ili, and abass from rain.csv
# remember all passwords are 4 digit


# Find all possible four-digit passwords =)
hash_pass_to_pass = {}
for password in range(1,10000):
    hashing_number = sha256(b'%i'% password).hexdigest()
    hash_pass_to_pass[hashing_number] = password

# now open file and read it
with open ('other/rain.csv')as f:
    password_singer = reader(f)
    for row in password_singer: #here we find passwords
        name_users = row[0]

        for key in row [1:]:
            print(name_users,":", hash_pass_to_pass[key])


