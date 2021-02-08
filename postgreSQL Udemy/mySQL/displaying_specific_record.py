# Displaying Specific Record


import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',db='crudpython')

myCursor=connection.cursor()

myCursor.execute("select * from record where Id='6'")

data=myCursor.fetchall()
print(data)

connection.commit()
connection.close()