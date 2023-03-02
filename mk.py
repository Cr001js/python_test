
count = 0
aval = 0
list= []
for i in range (1 , 2):
    number = int(input(''))
    for i in range (1, number + 1):
        if number % i == 0:
            list.append(i)
           
            aval = number % i
            count += 1
            

print(list)

print('count is :' , count)


