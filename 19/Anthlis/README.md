#Anthlis Amazing Weather Script

-------
####Prerequisites:

```
(venv) $ pip install -r requirements.txt
```
Two API keys are required: 
[GoogleV3 Geocode API](https://developers.google.com/maps/documentation/geocoding/intro) to POST your entered location, and the [DarkSky API](https://darksky.net/dev) to get the weather for the location.

Both API's are free to use once registered.  

API keys should be entered into a ```.env``` file.

----

When I started learning Python, this was one of the first scripts I ever wrote from scratch! 

It's really simple; it asks for a location and then prints out the weather in the following format: 

```
Enter a location: Auckland

>>> The wind in Auckland, New Zealand is currently 6.6 kts, and the direction is coming from 181 degrees.
>>> Set the altimeter to:  1019 HPa
>>> cloudy today!
```

The format was designed this way for me to quickly check the windspeed, pressure and general weather before I went flying. 

It's a script I still use today as most of the code now lives in a Flask web app I've dedicated to my private flying.   

@anthlis


