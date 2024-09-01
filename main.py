from flask import Flask, render_template, request  # Import necessary modules
from weather import weather  # Import weather function from weather module
from waitress import serve  # Import serve function from waitress module
import os  # Import os module

app = Flask(__name__)  # Create a Flask application instance
API_KEY = os.getenv("API_KEY")  # Get API key from environment variable

@app.route('/')  # Define route for home page
@app.route('/index')  # Define route for index page
def index():
    return render_template('index.html', api_key=API_KEY)  # Render index.html template with API key

@app.route('/weather')  # Define route for weather page
def get_weather():
    city = request.args.get('city')  # Get city parameter from request query string

    if not bool(city.strip()):  # Check if city parameter is empty or contains only whitespace
        city = 'Alexandria'  # Set default city to 'Alexandria'

    weather_data = weather(city)  # Call weather function to get weather data for the city

    if (weather_data['cod'] == '404' or weather_data['cod'] == '400'):  # Check if weather data contains error code
        return render_template('error.html', api_key=API_KEY)  # Render error.html template with API key

    return render_template (
        "weather.html",
        title = weather_data["name"],  # Pass weather data to weather.html template
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}",
        humidity = weather_data['main']['humidity'],
        wind_speed = weather_data['wind']['speed'],
        api_key=API_KEY
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port =8000)  # Start the server and listen on port 8000
