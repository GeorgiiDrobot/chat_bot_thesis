import sqlite3 

conn = sqlite3.connect('shop.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         name       TEXT    NOT NULL,
         description         TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         productID         TEXT    NOT NULL,
         img         TEXT    NOT NULL,
         cat        TEXT    NOT NULL

);''')#name,description,price,productID,img,cat
print ("Table created successfully")

conn.close()
