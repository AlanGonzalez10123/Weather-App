from flask import Flask

app = Flask(__name__)

@app.route('/')
def weather():
    return "Current weather is: "