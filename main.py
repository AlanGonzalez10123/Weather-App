from flask import Flask, render_template, request
from weather import weather
from waitress import serve
import os

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', api_key=API_KEY)

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = 'Alexandria' #DEFAULT

    weather_data = weather(city)

    if (weather_data['cod'] == '404' or weather_data['cod'] == '400'):
        return render_template('error.html', api_key=API_KEY)

    return render_template (
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}",
        humidity = weather_data['main']['humidity'],
        wind_speed = weather_data['wind']['speed'],
        api_key=API_KEY
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port =8000)
