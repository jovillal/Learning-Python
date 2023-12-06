#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:24:43 2020

@author: jovillal

Another dictionary, this from a remote SQL database
"""

import mysql.connector

#this opens the connection
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database",)

cursor = con.cursor()

#This fetches all the database (the result is a list of tuples)
#query = cursor.execute("SELECT * FROM Dictionary")
#results = cursor.fetchall()
#print(results)

#This fetches only one "word"
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")
#results = cursor.fetchall()
#print(results)

# A more interactive program
word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for r in results:
        print(r[1])
else:
    print("No word found!")