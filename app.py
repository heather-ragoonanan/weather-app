from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = '035d0705de3268331f77680311793506'

@app.route('/')
def home():
    return """
    <h1>Hello! This is my weather app.</h1>
    <form action="/weather">
        <input type="text" name="city" placeholder="Enter city name">
        <button type="submit">Get Weather</button>
    </form>
    """

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.ok:
        data = response.json()
        temperature = data['main']['temp']
        return f"The temperature in {city} is {temperature}°C"
    else:
        return "Sorry, no weather report found!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


