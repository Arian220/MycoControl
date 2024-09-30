from flask import Flask, render_template, redirect, url_for # type: ignore
#from flask_mysqldb import MySQL # type: ignore
#import MySQLdb.cursors # type: ignore
#import streamlit as st # type: ignore

app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'ari'
#app.config['MYSQL_PASSWORD'] = 'hernandezarian320'
#app.config['MYSQL_DB'] = 'your_database'

#mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@app.route('/psychrometric')
def psychrometric():
    return render_template('psychrometric.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    app.run(debug=True)