import sqlite3 

conn = sqlite3.connect('data.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         username        TEXT    NOT NULL,
         date         TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         orderid         TEXT    NOT NULL,
         status         TEXT    NOT NULL,
         payment        TEXT    NOT NULL,
         pname         TEXT    NOT NULL,
         productID        TEXT    NOT NULL,
         aa         TEXT    NOT NULL,
         bb         TEXT    NOT NULL,
         uname         TEXT    NOT NULL,
         address         TEXT    NOT NULL,
         nmbr         TEXT    NOT NULL,
         dtime         TEXT    NOT NULL,
         ct       TEXT    NOT NULL

);''')#ID,username,date,price,orderid,status,payment,pname,productID,aa,bb,cc
print ("Table created successfully")

conn.close()
