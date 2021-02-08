import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='create_table_postgreSQL'user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

def insert(roll,name,mark):
    conn = psycopg2.connect("dbname='create_table_postgreSQL'user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll,name,mark))
    conn.commit()
    conn.close()

insert(1,'pugger',1001)