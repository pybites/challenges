import json
import requests
import datetime
import os

import yaml # import env variables

DATE_FORMAT = '%b %d, %Y at %H:%M'

# If you want to test an url call you can use the command: curl 'URL' | jq | less
# You can learn more about requests here: https://requests.readthedocs.io/en/master/

def weather(app_id:str):
    input_val = input("What city do you want to look for? Send 'e' to end.").strip().capitalize()
    while input_val != 'E':
        payload = {'q': input_val, 'appid': app_id}
        r = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)
        data = json.loads(r.text)

        while data["cod"] != "200":
            print(f"Error: {data['message']}")
            input_val = input("Try again. What city do you want to look for? Send 'e' to exit.").strip().capitalize()
            if input_val == 'E':
                exit()
            payload = {'q': input_val, 'appid': app_id}
            r = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)
            data = json.loads(r.text)

        latitude = data["city"]["coord"]["lat"]
        longitude = data["city"]["coord"]["lon"]
        latest_date = data["list"][0]
        my_date = datetime.datetime.fromtimestamp(latest_date['dt']).strftime(DATE_FORMAT)

        print()
        print(f"On {my_date} {data['city']['name']} had {latest_date['weather'][0]['description']} with "
              f"{latest_date['clouds']['all']}% cloud cover.")
        print(f"The temperature was {latest_date['main']['temp']} although it felt like "
              f"{latest_date['main']['feels_like']} with a humidity of {latest_date['main']['humidity']}.")
        print(f"{data['city']['name']} is located at a latitude of {latitude} and a longitude of {longitude}.")
        print(f"It currently has a population of {data['city']['population']} people.")

        curr_datetime = datetime.datetime.now()
        two_years_ago = curr_datetime - datetime.timedelta(days=2*365)
        payload = {'appid': app_id, 'lat': latitude, 'lon': longitude, 'cnt': 5, 'start':
            (two_years_ago - datetime.datetime(1970, 1, 1)).total_seconds(), 'end':
            (curr_datetime - datetime.datetime(1970, 1, 1)).total_seconds()}
        r = requests.get('http://api.openweathermap.org/data/2.5/uvi/forecast', params=payload)
        uv_data = json.loads(r.text)
        print(f"The latest UV index for {data['city']['name']} was {uv_data[len(data)-1]['value']} taken on "
            f"{datetime.datetime.fromtimestamp(uv_data[len(data)-1]['date']).strftime(DATE_FORMAT)}.")
        print()

        input_val = input("Do you want to search for another? If so enter the city name; otherwise hit 'e' to exit.")\
            .strip().capitalize()


if __name__ == "__main__":
    with open(f"{os.environ['HOME']}/.config/CONFIG_FILENAME_NEEDED.yaml", 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # Need to get your APPID from https://openweathermap.org. I stored mine in my config file
    open_weather_key = config['open-weather']['api-key']

    weather(open_weather_key)