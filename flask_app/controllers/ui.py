from flask_app import app
from flask import render_template, redirect
from flask_app.models.users import User

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def readall():
    return render_template('Read_All.html', users = User.get_all_users())