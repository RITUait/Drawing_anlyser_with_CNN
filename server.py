# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:51:03 2018

@author: abhi
"""

from flask import Flask  
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    message = "Hello, World"
    return render_template('home.html', message=message)

# run the application
if __name__ == "__main__":  
    app.run(debug=True,port = 50023)