import mysql.connector

# data = input()
cnx = mysql.connector.connect(user= 'root', password = '', database = 'truecar', host= '127.0.0.1')
cursor = cnx.cursor()


for i in range(1):
    name = ['ford']
    miles = ['2000 miles']
    price = ['$2983']

    cursor.execute('INSERT INTO truecar VALUES(\'%s\', \'%s\', \'%s\')' % (name[i], miles[i], price[i]))



cnx.commit()
cnx.close()


