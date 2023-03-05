# this is a simple code
# This code finds all prime numbers
x = int(input(""))

if x > 1:
    for i in range (2, x):
        if (x % i) == 0:
            print(x, 'no')
            break
    else:
        print(x, 'yes')
    