from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import User

@app.route('/create-user')
def r_create_song():
    return render_template('create.html')

@app.route('/create_user', methods = ['POST'])
def f_create_user():
    User.insert_user(request.form)
    return redirect('/users')

@app.route('/user/show_one/<int:id>')
def show_one_user(id):
    data = {
        "id":id
    }
    return render_template('Read_One.HTML', user=User.show_one(data))

@app.route ('/user/edit_one/<int:id>')
def edit_one_user(id):
    data = {
        "id":id
    }
    return render_template('Edit_One.HTML', user=User.show_one(data))

@app.route ('/user/update', methods = ['POST'])
def update_users():
    User.update_one(request.form)
    return redirect('/')

@app.route ('/user/delete/<int:id>')
def delete_this_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect('/')