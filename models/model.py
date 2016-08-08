from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:{}@localhost/restaurantmap'.format(os.environ.get('DB_PASSWORD'))
db = SQLAlchemy(app)



##Base = declarative_base()

#Create a class for the restaurant data
class Restaurant(db.Model):
##class Restaurant(Base):
#    __tablename__ = 'Restaurants'
#    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    obj_id = Column(String(20))
    name = Column(String)
    building = Column(Integer)
    zip_code = Column(String)
    longitude = Column(String)
    latitude = Column(String)

    def __init__(self,obj_id, name, building, zip_code, longitude, latitude):
        self.obj_id = obj_id
        self.name = name
        self.building = building
        self.zip_code = zip_code
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return "<Restaurant(name='%s', latitude='%s, longitude='%s')>" % (self.name, self.latitude, self.longitude)

db.create_all()

'''
if __name__ == "__main__":

    #Create the database
    engine = create_engine('sqlite:///restaurant_coords.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker(bind=engine)
    s = session()

    try:
        with open('/home/jean/PythonMapMakers/models/restaurants.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)

        for i in data:
            record = Restaurant(**{
                'obj_id' : i[0],
                'name' : i[1],
                'building' : i[2],
                'zip_code' : i[3],
                'longitude' : i[4],
                'latitude' : i[5]
            })
            s.add(record) #Add all the records
            s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
'''
