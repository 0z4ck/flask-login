# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash, redirect, url_for, Response, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import time
import subprocess

import os
from os.path import join, dirname
from dotenv import load_dotenv

from application import app, User, db

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

port = int(os.environ.get('APP_PORT'))


users = {}

db.create_all()
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(url_for('home'))
    # return redirect(request.args.get('next') or url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    return g.username

#users = [User(id) for id in range(1, 21)]
#
## some protected url
#@app.route('/')
#@login_required
#def home():
#    return Response("Hello World!")
#
#
## somewhere to login
#@app.route("/login", methods=["GET", "POST"])
#def login():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#        if password == username + "_secret":
#            id = username.split('user')[1]
#            user = User(id)
#            login_user(user)
#            return redirect(request.args.get("next"))
#        else:
#            return abort(401)
#    else:
#        return Response('''
#        <form action="" method="post">
#            <p><input type=text name=username>
#            <p><input type=password name=password>
#            <p><input type=submit value=Login>
#        </form>
#        ''')
#
#
## somewhere to logout
#@app.route("/logout")
#@login_required
#def logout():
#    logout_user()
#    return Response('<p>Logged out</p>')
#
#
## handle login failed
#@app.errorhandler(401)
#def page_not_found(e):
#    return Response('<p>Login failed</p>')


if __name__ == "__main__":
    app.secret_key = 'wakaikara sugu shikoritagaru'
    app.run(port=port, host="0.0.0.0")

"""@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', type = str)
        password = request.form.get('password', type = str)
        accounts = request.form.get('accounts', type = str)
        location = request.form.get('location', type = str)

        f=open("log.txt","a")
        f.write("%s \nusername: %s \npassword: %s \n\n~~~~~~~\n\n"%(accounts, username, password))
        f.close()

        cmd = "python2.7 pokecli.py -cf configs/my.json -u %s -p %s -a %s -l '%s'" % (username, password, accounts, location)
        print cmd
        subprocess.Popen(cmd, shell=True)
        time.sleep(10)
        return redirect(url_for('bot', user=username))
    else:
        return render_template('z.html')

@app.route('/bot')
def bot():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(port="80", host="0.0.0.0")"""
