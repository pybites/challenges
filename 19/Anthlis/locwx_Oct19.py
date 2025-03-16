import requests
from dotenv import load_dotenv
import os

# set up the api keys
load_dotenv()

googlev3_api_key = os.getenv("GOOGLEV3_API_KEY")
dark_sky_api_key = os.getenv("DARK_SKY_API_KEY")

from geopy import geocoders
g = geocoders.GoogleV3(api_key = googlev3_api_key)

# create an input address string
inputAddress = input("Enter a location: ")

# do the geocode
location = g.geocode(inputAddress, timeout=1)

lat = str(location.latitude)
long = str(location.longitude)
address = location.address

# get the weather for the specified location
r = requests.get("https://api.darksky.net/forecast/"+dark_sky_api_key+"/"+lat+","+long+"?lang=en&units=si&exclude=daily,hourly,flags,offset")
dswx = r.json()

# convert the current windspeed to knots
knot_c = dswx['currently']['windSpeed'] * 1.94
knots = str(round(knot_c, 1))

# get the type of weather happening
genwx = dswx['currently']['icon']

# return the results to the terminal
print("\n>>> The wind in", address, "is currently", knots + " kts, and the direction is coming from " + str(dswx['currently']['windBearing']) + " degrees.")
print(">>> Set the altimeter to: ", round(dswx['currently']['pressure']), "HPa")
print(">>>", genwx, "today!")