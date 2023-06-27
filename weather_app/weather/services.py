import requests

def get_weather_data(city):
	api_key = '4caa43995aea7d32d221a6cec21b2134'
	base_url ='http://api.openweathermap.org/data/2.5/weather'

	params = {
	     'q' : city,
	     'appid' : api_key,
	     'units' : 'metric'
	}

	try:
		response = requests.get(base_url, params= params)
		response.raise_for_status()
		data = response.json()
		

		weather = {
			'temperature' : data['main']['temp'],
			'description' : data['weather'][0]['description'],
			'humidity': data['main']['humidity'],
			'wind_speed' : data['wind']['speed'],
		}

		return weather
	except requests.exceptions.RequestException as e:
		print("Error featching weather data: {e}")
		return None
