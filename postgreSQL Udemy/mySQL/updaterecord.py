# Update Record (Update Query in MySQL)

import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',db='crudpython')

myCursor=connection.cursor()

myCursor.execute("update record set Name='Camille Hernandez', Mobile='09072191005', Address='Pampanga' where Id='10'")

print ("Record Updated Successfully!")

connection.commit()
connection.close()