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

# enable debugging
app.config['DEBUG'] = True

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_word():
    return "Hello, World!?Joel?!!!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# test integers
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct path"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404
    
# start the development server using the run() method
if __name__ == '__main__':
    app.run()