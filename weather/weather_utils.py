import requests

from weatherapp import settings

class WeatherMixin:
    def __init__(self):
        self.extra_context = {}

    def get_city_weather(self, city):
        api_key = settings.API_KEY
        cleaned_data = city
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cleaned_data}&appid={api_key}"
        response = requests.get(url)
        weather_data = response.json()
        if self.extra_context is not None:
            self.extra_context['weather_data'] = weather_data
        else:
            self.extra_context = {'weather_data': weather_data}
        return self.extra_context

