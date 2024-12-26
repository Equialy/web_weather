from weather.repositories.weather_repository import LocationsRepository
from weather.services.weather_services import WeatherDatabaseService, WeatherAPIService


class Services:
    def __init__(self):
        self.weather_db_service = WeatherDatabaseService(LocationsRepository())
        self.weather_api_service = WeatherAPIService()

    def database_service(self):
        return self.weather_db_service

    def api_service(self):
        return self.weather_api_service


services = Services()
