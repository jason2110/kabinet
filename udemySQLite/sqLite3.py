import sqlite3

def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)") # `bactic to seperate things`
    conn.commit()
    conn.close()

def insert(roll,name,mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,name,mark))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(roll):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?", (roll,))
    conn.commit()
    conn.close()

def update(name,mark,roll):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=? , marks=? WHERE rollno=?",(name,mark,roll))
    conn.commit()
    conn.close()

#update('super',56,4)

print(view())