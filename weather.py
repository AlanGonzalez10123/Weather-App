from flask import Flask
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def weather(city="Alexandria"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather = requests.get(request_url).json()

    return weather

if __name__ == "__main__":
    print('\n***Get Current Weather***\n')
    city = input("\nEnter a city name: ")

    weather_data = weather(city)

    print("\n")
    pprint(weather_data)