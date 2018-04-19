#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:50:40 2018

@author: aaronjoel
"""

# SELECT statement

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    
    # use a for loop to iterate through the database, printing the results
    # line by line.
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)