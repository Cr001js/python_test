a = input('')

def captial_indexes(a):
    list = [*a]
    count = -1
    l = []
    for i in list:
        count += 1
        if i.isupper() == True:
            l.append(count)
    print(l)    

captial_indexes(a)