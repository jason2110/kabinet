#Crud operation in Python using MySQL

import pymysql

connection = pymysql.connect (host='localhost', user='root', password='', db='crudpython')

myCursor=connection.cursor ()
myCursor.execute ("insert into record (Name,Mobile,Address) value ('Jason Dungca', '09155517080', 'Philippines')")

print ("Data Inserted Successfully")

connection.commit ()
connection.close ()
