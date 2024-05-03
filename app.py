from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

# create an instance of the Flask class
app = Flask(__name__)

#home route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Home Page")

@app.route('/about')
def about():
    return render_template('about.html', title = "About Page")

@app.route('/contact')
def contact():
    return render_template('contact.html', title = "Contact Page")


# to run the flask app
if __name__== "__main__":
    app.run(debug=True)