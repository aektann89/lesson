import requests
import os

def get_weather():

    city = input()
    key = os.environ.get('api_key')
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)

    weather = result.json()

    print(f'''{str(weather["name"])}:
Temperature: {weather["main"]["temp"]}C
Feels like: {weather["main"]["feels_like"]}C
Pressure: {weather["main"]["pressure"]}mm
Humidity: {weather["main"]["humidity"]}%
Wind: {weather["wind"]["speed"]}m/s
''')

get_weather()