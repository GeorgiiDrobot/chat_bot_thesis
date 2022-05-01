import sqlite3 

conn = sqlite3.connect('cat.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         cat          TEXT    NOT NULL,
         des          TEXT    NOT NULL

);''')
print ("Table created successfully")