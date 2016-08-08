from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/submitsurvey', methods=['POST'])
def submitsurvey():
   print(request.form)
   price = request.form.get("price")
   rating = request.form.get("rating")
   latitude = float(request.form.get("latitude"))
   longitude = float(request.form.get("longitude"))
   comments = request.form.get("comments")
   DB.restaurantmap(price, rating, latitude, longitude, comments)
   return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
