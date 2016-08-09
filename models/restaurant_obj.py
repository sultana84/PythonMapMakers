from model import Restaurant, db
import csv

with open('/home/jean/PythonMapMakers/models/restaurants.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    for i in data[1:]:
        record = Restaurant(**{
            'obj_id': i[0],
            'name': i[1],
            'building': i[2],
            'zip_code': i[3],
            'longitude': float(i[4]),
            'latitude': float(i[5])
        })

        db.session.add(record)
        db.session.commit()
