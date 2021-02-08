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

def view():
    conn = psycopg2.connect("dbname='create_table_postgreSQL'user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(roll):
    conn = psycopg2.connect("dbname='create_table_postgreSQL'user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s", (roll,))
    conn.commit()
    conn.close()

delete(2)