maghsoms = [3, 419, 1257]
aval = 0
# maghsoms = [1, 2, 3, 4, 6, 8]
for i in maghsoms:
    num = i
    flag = False
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        print(num, 'is not')
        

    else :
        print(num, 'is')
        aval += 1

print(aval)