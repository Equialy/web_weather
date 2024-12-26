import logging

import requests
from core import settings
from weather.repositories.weather_repository import LocationsRepository
from weather.services import handlers

logger = logging.getLogger('web')


class WeatherAPIService:

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

    def get_mixin_context(self, context, data, **kwargs):
        """Добавляем контекст для страницы"""

        context['weather_data'] = data
        context['city'] = data['weather_data']['name']
        context['temp_min'] = handlers.kelvins_to_celsious(data['weather_data']['main']['temp_min'])
        context['temp_max'] = handlers.kelvins_to_celsious(data['weather_data']['main']['temp_max'])
        context['current_temp'] = handlers.kelvins_to_celsious(data['weather_data']['main']['feels_like'])
        context['feels_like'] = handlers.kelvins_to_celsious(data['weather_data']['main']['feels_like'])
        context['get_lon'] = round(data['weather_data']['coord']['lat'], 5)
        context['get_lat'] = round(data['weather_data']['coord']['lon'], 5)

        context.update(kwargs)

        return context

    def index_queryset(self, context, **kwargs):
        """ Создаем queriset на стринице выдачи после поиска """
        updated_data = []
        for item in context:
            if item and 'weather_data' in item:
                try:

                    city_data = {
                        'city': item['weather_data']["name"],
                        'temp_min': handlers.kelvins_to_celsious(item['weather_data']['main']['temp_min']),
                        'temp_max': handlers.kelvins_to_celsious(item['weather_data']['main']['temp_max']),
                        'current_temp': handlers.kelvins_to_celsious(item['weather_data']['main']['feels_like']),
                        'feels_like': handlers.kelvins_to_celsious(item['weather_data']['main']['feels_like']),
                        'get_lon': round(item['weather_data']['coord']['lon'], 5),
                        'get_lat': round(item['weather_data']['coord']['lat'], 5),
                    }
                    city_data.update(kwargs)
                    updated_data.append(city_data)
                except KeyError as e:
                    logger.debug(f"Key error {e}")

        return updated_data


class WeatherDatabaseService:

    def __init__(self, locations_repo: LocationsRepository):
        self.locations_repo: LocationsRepository = locations_repo

    def get_all_locations(self):
        stmt = self.locations_repo.find_all()
        return stmt

    def save_location(self, city, latitude, longitude, user):
        self.locations_repo.add_one(city=city, latitude=latitude, longitude=longitude, user=user)

    def get_location(self, id, userid):
        self.locations_repo.get_one(id, userid)

    def delete_location(self, pk):
        self.locations_repo.delete_one(pk)
