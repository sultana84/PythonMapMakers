from flask import Flask, render_template, flash
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user, logout_user
from flask import redirect
from flask import url_for
from flask import request
from dbhelp import dbhelp as DBHelper
from model import User
from passwordhelp import PasswordHelp
import os
from model import app, db
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


login_manager = LoginManager(app)
login_manager.login_view = 'login'

#client = MongoClient()


@app.route("/")
@login_required
def home():
    return render_template("home.html")


@app.route('/home')
@login_required
def surveyhome():
    return render_template("surveyhome.html")

@app.route('/submitsurvey', methods=['POST'])
@login_required
def submitsurvey():
   price = request.form.get("price")
   rating = request.form.get("rating")
   latitude = float(request.form.get("latitude"))
   longitude = float(request.form.get("longitude"))
   comments = request.form.get("comments")
   DB.restaurantmap(price, rating, latitude, longitude, comments)
   return render_template("surveyhome.html")

@app.route("/account", methods=[ "GET", "POST"])
@login_required
def account():
    return render_template("account.html")

@app.route("/login", methods=[ "GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form.get("username")
    password = request.form.get("password")
    registered_user = User.query.filter(User.email==email).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('register'))
    if registered_user.password and registered_user.check_password(password):
        print('LOGGED IN')
        login_user(registered_user, remember=True)
        return redirect(url_for('surveyhome'))
    else:
        print('NOT LOGGING IN')
        flash('A user was not found with that username and password combination')
        return render_template('surveyhome.html')

@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form.get('email')
    pw1 = request.form.get('password1')
    pw2 = request.form.get('password2')
    if not pw1 == pw2:
        flash("Password do not match")
        return redirect(url_for("register"))
    else:
        password = pw1

    if User.query.filter(User.email == email).count():
        flash("This email already register!")
        return redirect(url_for("login.html"))
    user = User(password, email)
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    login_user(user)
    return redirect(url_for('login'))


'''

    registered_user = Use(str(request.form.get))
#    db.session.add(user)
#    db.session.commit()
#    flash('User successfully registered')
#    return redirect(url_for('login'))
    email = str(request.form.get["email"])
    pw1 = str(request.form.get["password"])
    pw2 = str(request.form.get["password2"])
    if not pw1 == pw2:
        return redirect(url_for("home"))
    if DB.get_user(email):
        return redirect(url_for("home"))
    salt = PH.get_salt()
    hashed = PH.get_hash(pw1 + salt)
    DB.add_user(email, salt, hashed)
    return redirect(url_for("home"))
'''



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id==user_id)



app.secret_key = '0ZyLk/0K1+GVdZTRWCfK441+CUHGmRKXzly1UXnws29VOYHuVTCyhFfMh4c9OcWUgL8iGgk5a99t9T1Xo5EsC9wmoTAiDPZu8US'

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')

