import requests
from .service_handler import handlers
from weatherapp import settings


class WeatherMixinAPI:
    def __init__(self):
        self.extra_context = {}


    def get_city_weather(self, city):
        """Запрос к API"""
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


class GetContextAPI(WeatherMixinAPI):

    def get_mixin_context(self, context, city_request, **kwargs):
        """Для добавления контекста"""
        context['weather_data'] = city_request
        context['temp_min'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['temp_min'])
        context['temp_max'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['temp_max'])
        context['current_temp'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['feels_like'])
        context['feels_like'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['feels_like'])
        context['get_lon'] = round(self.extra_context['weather_data']['coord']['lat'], 5)
        context['get_lat'] = round(self.extra_context['weather_data']['coord']['lon'], 5)



        context.update(kwargs)
        return context

