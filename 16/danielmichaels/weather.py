from api_secrets import WEATHER_TOKEN
from utils import datetime_helper
import requests
import requests_cache
import logging

logging.basicConfig(level=logging.INFO)


class Weather:
    """A simple class that pulls in weather data from the openweathermap api
    and formats the response into Discord readable markdown.

    """

    def __init__(self, city='perth', country='AU'):
        self.city = city
        self.country = country
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city}," \
                   "{country}&units=metric&appid={TOKEN}".format(
            city=self.city, country=self.country, TOKEN=WEATHER_TOKEN)

    def get_data(self):
        """Get the weather data in JSON format. Caches the response for
        600 seconds in a sqlite database.

        """
        logging.info(self.url)
        requests_cache.install_cache(expire_after=600)
        response = requests.get(self.url)
        if response.status_code != 200:
            logging.error("API did not return status code of 200")
        data = response.json()
        return data

    def format(self, data):
        """Parse out wanted weather info.

        :arg data: required from get_data method.

        :return output in markdown.

        """
        location, cc = data['name'], data['sys']['country']
        temp = data['main']['temp']
        conditions = [item['description'] for item in data['weather']][0]
        time = data['dt']
        local_time = datetime_helper(time)
        output = """
        __**WEATHER REPORT**__\n
        *{0}, {4}*
        Temp:\t **{1}**
        Conditions:\t {2}
        As At:\t **{3}**
        """.format(location, temp, conditions, local_time, cc)
        return output
