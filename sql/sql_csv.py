#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:29:33 2018

@author: aaronjoel
"""

# import from CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
    
    c = connection.cursor()
    
    # open the csv file and assign it to a variable
    employees = csv.reader(open("/home/aaronjoel/Documents/2018/RealPython/book2-exercises/sql/employees.csv", "rU"))
    
    # create a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    
    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)
    