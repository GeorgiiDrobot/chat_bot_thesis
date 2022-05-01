import sqlite3

conn = sqlite3.connect('cart.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         name   TEXT    NOT NULL,
         productID   TEXT    NOT NULL,
         price   TEXT    NOT NULL,
         quantity   TEXT    NOT NULL
     
);''')#ID,name,productID,price,quantity
print ("Table created successfully")
conn.close()