#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:35:32 2021

Stuff for data base management or use

@author: jovillal
"""

import sqlite3 #this is native library for interacting via SQLite 

conn = sqlite3.connect("lite.db")  #This connects to the db lite.db, if it doesn't exist it is created.
cur = conn.cursor()  #This creates a cursor on the db

"""
This is how SQL commands are used, they go between quotes. 
keywords should be CAPITALIZED
Here we create a table named "store" with 3 columns:
  item, which is a string
  quantity, an integer
  price, float
If the db exists it is not created
"""
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL )") 

"""
This insterts data into the database

    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")

To use values from a function do the following
"""
def insert(item, quantity, price):
    cur.execute("INSERT INTO store VALUES (?, ?, ?)",(item, quantity, price))
    #careful, if only one parameter is passed the syntaxt is:
    #cur.execute("INSERT INTO store VALUES ?",(var,))
    #there is an extra ","

insert("Coffe cup",3,4.5)

conn.commit() #commits the changes 

cur.execute("SELECT * FROM store") #This reads all the db
rows = cur.fetchall() #this returns the db as a list

conn.close() #closes the connection

print(rows)
"""
To delete a row using the information from a column (the name is colname)
    DELETE FROM dbasename WHERE colname=rowitem
To update values from a row where col1, col2, and col3 are columns
    UPDATE dbasename SET col2 = ?, col3 = ? WHERE col1 = ?

"""



