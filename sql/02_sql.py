#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:08:02 2018

@author: aaronjoel
"""

# INSERT Command

# import the sqlite3 libary
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('NEW York City', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('SAN Francisco', 'CA', 8000000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()