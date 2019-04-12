#run export FLASK_ENV=development before running flask run
import datetime, requests
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

key = open("apikey.txt","r").readline()
url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID='+key
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'


db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()
        
    cities = City.query.all()
    weather_data = []
    weather= dict()

    for city in cities:
        response = requests.get(url.format(city.name)).json()
        if response['cod'] == '404':
            city_obj = City.query.filter_by(name=city.name).first()
            db.session.delete(city_obj)
            db.session.commit()
        else:
            print(response)
            weather = {
                'time' : datetime.datetime.now().strftime("%H:%M:%S"),
                'city' : city.name ,
                'temperature' : response['main']['temp'],
                'description' : response['weather'][0]['description'].capitalize(),
                'icon': response['weather'][0]['icon']
            }
            weather_data.append(weather)
    return render_template('weather.html',weather_data = weather_data)

@app.route("/delete", methods=["POST"])
def delete():
    citytitle = request.form.get("citytitle")
    city = City.query.filter_by(name=citytitle).first()
    db.session.delete(city)
    db.session.commit()
    return redirect("/")

