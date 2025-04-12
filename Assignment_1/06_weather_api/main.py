import requests
from pprint import pprint

api_key = '2944c1fcbbbf57dd1950b13426c26ad8'
user_city = input('Enter your City: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric'

weather_data =requests.get(url).json()
pprint(weather_data)