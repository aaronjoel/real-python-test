#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:36:25 2018

@author: aaronjoel
"""

# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8000000)")
    
    # commit the changes
    conn.commit()
    
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

# close the database connection
conn.close()