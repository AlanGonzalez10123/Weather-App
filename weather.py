from flask import Flask  # Importing the Flask module for creating a web application
from dotenv import load_dotenv  # Importing the load_dotenv function from the dotenv module for loading environment variables from a .env file
from pprint import pprint  # Importing the pprint function from the pprint module for pretty-printing data structures
import requests  # Importing the requests module for making HTTP requests
import os  # Importing the os module for interacting with the operating system

load_dotenv()  # Loading environment variables from a .env file

def weather(city="Alexandria"):
    """
    Function to get weather data for a given city.
    :param city: The name of the city for which weather data is requested (default is "Alexandria")
    :return: The weather data as a dictionary
    """
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    # Constructing the request URL with the API key and the city name

    weather = requests.get(request_url).json()  # Sending a GET request to the OpenWeatherMap API and getting the response as JSON

    return weather  # Returning the weather data as a dictionary

###FOR CONSOLE TESTING###
if __name__ == "__main__":
    print('\n***Get Current Weather***\n')
    city = input("\nEnter a city name: ")

    if not bool(city.strip()):
        city = "Alexandria" #Default Value

    weather_data = weather(city)

    print("\n")
    pprint(weather_data)