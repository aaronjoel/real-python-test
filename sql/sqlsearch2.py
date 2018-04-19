#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:53:54 2018

@author: aaronjoel
"""

# SELECT statement, remove unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname from employees")
    # fetchall() retrieves all records from the query
    rows = c.fetchall()
    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])