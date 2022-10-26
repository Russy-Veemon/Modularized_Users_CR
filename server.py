from flask import Flask, render_template, session, redirect, request
from users import User

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def readall():
    return render_template('readall.html', users = User.get_all_users())

@app.route('/create-user')
def r_create_song():
    return render_template('create.html')

@app.route('/create_user', methods = ['POST'])
def f_create_user():
    User.insert_user(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)