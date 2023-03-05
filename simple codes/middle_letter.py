# this code will show you middle letters
# and if text have no middle letters, returns NO

a = input('')
k = len(a)
len = len(a) - 1
len = len // 2
k = k // 2
if k % 2 == 0:
    print('NO')
else: 
    print((a[len]))