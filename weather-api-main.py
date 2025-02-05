from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_weather_api_key'  # Replace with your actual weather API key
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'  # Replace with your actual weather API URL

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')

    if not location:
        return 'Location query parameter is required', 400

    try:
        response = requests.get(WEATHER_API_URL, params={
            'key': API_KEY,
            'q': location
        })
        response.raise_for_status()
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data: {e}')
        return 'Error fetching weather data', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
