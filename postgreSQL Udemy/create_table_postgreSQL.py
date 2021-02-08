import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='create_table_postgreSQL'user='admin' password='admin' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)") # `bactic to seperate things`
    conn.commit()
    conn.close()

createtable()