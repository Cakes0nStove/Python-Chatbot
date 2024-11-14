import datetime as dt
from http.client import responses

import requests

def weatherapp():

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open('api_key', 'r').read()
    input_location = input('Input City to view weather forecast ->' )
    CITY = input_location

    def converttoC(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) +32
        return celsius, fahrenheit

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = converttoC(temp_kelvin)
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description']
    sunrise = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f'temperature in {CITY}: {temp_celsius:.2f}C')
    print(f'The wind speed in {CITY}: {wind_speed}' )
    print(f'The weather description {CITY}: {description}')
    print(f'Sunrise time in {CITY} : {sunrise}')
    print(f'Sunrise time in {CITY} : {sunset}')
