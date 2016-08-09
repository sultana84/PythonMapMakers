from flask import Flask, render_template, flash
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user, logout_user
from flask import redirect
from flask import url_for
from flask import request
from dbhelp import dbhelp as DBHelper
from user import User
from passwordhelp import PasswordHelp
from pymongo import MongoClient
import os

DB = DBHelper()
PH = PasswordHelp()


app = Flask(__name__)
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
def submitsurvey():
   price = request.form.get("price")
   rating = request.form.get("rating")
   latitude = float(request.form.get("latitude"))
   longitude = float(request.form.get("longitude"))
   comments = request.form.get("comments")
   DB.restaurantmap(price, rating, latitude, longitude, comments)
   return home()


@app.route("/account", methods=[ "GET", "POST"])
#@login_required
def account():
    return render_template("account.html")

@app.route("/login", methods=[ "GET", "POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    user_password = DB.get_user(email)
    if user_password and user_password == password:
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return render_template('login-form.html')

@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
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

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)



app.secret_key = '0ZyLk/0K1+GVdZTRWCfK441+CUHGmRKXzly1UXnws29VOYHuVTCyhFfMh4c9OcWUgL8iGgk5a99t9T1Xo5EsC9wmoTAiDPZu8US'

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
