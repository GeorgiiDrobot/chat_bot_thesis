import sqlite3

conn = sqlite3.connect('orders.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         price   TEXT    NOT NULL,
         quantity   TEXT    NOT NULL,
         pname    TEXT    NOT NULL,
         status   TEXT    NOT NULL,
         payment   TEXT    NOT NULL,
         username   TEXT    NOT NULL,
         contact   TEXT    NOT NULL,
         orderID   TEXT    NOT NULL,
         uname   TEXT    NOT NULL,
         address   TEXT    NOT NULL,
         time   TEXT    NOT NULL,
         date  TEXT    NOT NULL
         
     
);''')#ID,price,quantity,status,pname,payment,username,contact,orderID,date
print ("Table created successfully")
conn.close()