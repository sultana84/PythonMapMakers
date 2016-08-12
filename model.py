from flask import Flask
import os

from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
import csv
import os
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask, render_template, flash
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user, logout_user
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost/restaurantmap'.format(os.environ.get('DB_PASSWORD'))
db = SQLAlchemy(app)


#from views import app



#login_manager = LoginManager(app)
#login_manager.login_view = 'login'

#client = MongoClient()

##Base = declarative_base()

#Create a class for the restaurant data
class Restaurant(db.Model):
##class Restaurant(Base):
    __tablename__ = 'Restaurants'
#    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    obj_id = Column(String(20))
    name = Column(String(150))
    building = Column(String(100))
    zip_code = Column(String(14))
    longitude = Column(Float)
    latitude = Column(Float)

    def __init__(self,obj_id, name, building, zip_code, longitude, latitude):
        self.obj_id = obj_id
        self.name = name
        self.building = building
        self.zip_code = zip_code
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return "<Restaurant(name='%s', latitude='%s, longitude='%s')>" % (self.name, self.latitude, self.longitude)



class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    password = db.Column('password' , db.String(200))
    email = db.Column('email',db.String(50),unique=True , index=True)

    def __init__(self, password, email):
        self.password = self.hash_password(password)
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.email)

    def hash_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


db.create_all()
