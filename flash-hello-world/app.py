#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:22:04 2018

@author: aaronjoel
"""

# --- Flask Hello World --- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_word():
    return "Hello, World! Joel"

# start the development server using the run() method
if __name__ == '__main__':
    app.run()