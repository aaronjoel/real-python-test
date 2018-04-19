#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:22:14 2018

@author: aaronjoel
"""

# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    
    c = connection.cursor()
    
    # insert multiple records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
            ]
    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)