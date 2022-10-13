import datetime
import sys

from api_secrets import WEATHER_TOKEN

import requests
import requests_cache

from requests.exceptions import RequestException


class Weather:
    """A simple class that pulls in weather data from the openweathermap api and formats the response.

    """

    def __init__(self, city="london", country="gb"):
        self.city = city
        self.country = country
        self.url = (
            "http://api.openweathermap.org/data/2.5/weather?q={city},"
            "{country}&units=metric&appid={TOKEN}".format(
                city=self.city, country=self.country, TOKEN=WEATHER_TOKEN
            )
        )
        self.get_data

    @property
    def get_data(self):
        """Get the weather data in JSON format. Caches the response for
        600 seconds in a sqlite database.

        """
        requests_cache.install_cache(expire_after=600)
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            return self.format(data)
        except requests.exceptions.RequestException as e:
            # for brevity don't try/except all possible cases
            print(f"[!] An Error Occurred [!]\n\n{e}")
            sys.exit(1)

    @staticmethod
    def client_localtime():
        """Return localtime."""
        return datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")

    def format(self, data):
        """Parse out wanted weather info.

        :arg data: required from get_data method.

        :return output in markdown.

        """
        location, cc = data["name"], data["sys"]["country"]
        temp = data["main"]["temp"]
        conditions = [item["description"] for item in data["weather"]][0]
        time = data["dt"]
        degrees = "\u00b0"

        output = f"""
        [*] {location}, {cc} [*]

        __WEATHER REPORT__\n
        Temp: {temp:.1f}{degrees + 'C'}
        Conditions: {conditions.title()}
        Last Updated: {self.client_localtime()} Local Time
        """
        print(output)
