#Crud operation in Python using MySQL

import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',db='routine')

myCursor=connection.cursor()
name=input("Enter your name :")
mobile=input("Enter your mobile number :")
address=input("Enter your address :")

query="insert into record(Name,Mobile,Address) value (%s,%s,%s)"
myCursor.execute(query,(name,mobile,address))
print("Data Inserted Successfully")

connection.commit()
connection.close()