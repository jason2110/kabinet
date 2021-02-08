# Deleting Record

import pymysql

connection=pymysql.connect(host='localhost',user='root',password='',db='crudpython')

myCursor=connection.cursor()
myCursor.execute("delete from record")

data=myCursor.fetchall()
print("Record Deleted Successfully!")

connection.commit()
connection.close()
