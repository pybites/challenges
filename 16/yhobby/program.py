from pprint import pprint
import os

from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_PASSWORD')

user_input = input('Please enter the Movie name: ')

payload = {'apikey': api_key,
           's': user_input}
url = 'http://www.omdbapi.com/'
response = requests.get(url, params=payload)
data = response.json()

movies = data['Search']

for idx, movie in enumerate(movies, 1):
    print('#' * 30)
    print(idx, ') ', movie['Title'], sep='')
    idx += 1
    print('#' * 30)
    for k, v in movie.items():
        print(k, '===>', v)
