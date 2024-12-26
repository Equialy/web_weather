from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView

from .models import Locations
from .repositories.weather_repository import LocationsRepository
from .services.cached_service import CacheService
from .services.weather_services import WeatherAPIService, WeatherDatabaseService
import logging
from django.core.cache import cache

logger = logging.getLogger('web')


def index(request):
    get_cities = WeatherDatabaseService(LocationsRepository()).get_all_locations()
    return render(request, "weather/index_home.html", {"weather_data": get_cities})


def get_city_weather(request):
    if request.method == "GET":
        city = request.GET.get('city')
        cached_data = CacheService().get_cached(city)
        if cached_data:
            logger.debug(f"Получены данные из кеша: {cached_data}")
            context = WeatherAPIService().get_mixin_context({}, cached_data)
            return render(request, 'weather/weather.html', {"weather": context})
        else:
            get_city_from_api = WeatherAPIService().get_city_weather(city)
            logger.debug(f"Данные из API: {get_city_from_api}")
            cached = CacheService().create_cache(city=city, data=get_city_from_api)
            context = WeatherAPIService().get_mixin_context({}, cached)
            return render(request, 'weather/weather.html', {"weather": context})

def save_to_db_location(request):
    if request.method == "POST":
        data_weather = {
            "city": request.POST.get('name'),
            "latitude": request.POST.get('latitude'),
            "longitude": request.POST.get('longitude'),
            "user": request.user
        }

        save_location_to_db = WeatherDatabaseService(LocationsRepository()).save_location(**data_weather)
        print(f"Данные из view save_to_db {save_location_to_db}")
        return redirect("weather:index")

def delete_location(request, pk):
    if request.method == "POST":
        user = request.user
        logger.debug(f"DELETE request received for pk={pk} by user={user}")
        # location = WeatherDatabaseService(LocationsRepository()).get_location(id=pk, userid=user)
        WeatherDatabaseService(LocationsRepository()).delete_location(pk)

        return redirect('weather:index')
    return redirect('weather:index')


class Index(ListView, WeatherAPIService):  # IndexContext
    template_name = 'weather/index_home.html'
    title_page = 'Главная страница'
    context_object_name = 'location_data'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Удаление из базы если нет в кеше
            cached_cities = cache.get('cached_cities', [])
            cities_in_db = Locations.objects.values_list('name', flat=True)
            cities_to_delete = [city for city in cities_in_db if city not in cached_cities]
            Locations.objects.filter(name__in=cities_to_delete).delete()

            return Locations.objects.filter(userid=self.request.user)
        else:
            return Locations.objects.none()

    def get_context_data(self, **kwargs):
        """Добавляем данные из кеша в контекст"""
        context = super().get_context_data(**kwargs)

        cached_cities = cache.get('cached_cities', [])
        cached_weather_data = [cache.get(f'cached_city_{city}') for city in cached_cities]
        context_weather = self.index_queryset(cached_weather_data)
        context['weather_data'] = context_weather

        return context


class GetCityWeather(TemplateView, WeatherAPIService):  # GetContextAPI
    template_name = 'weather/weather.html'
    model = Locations

    def get_context_data(self, **kwargs):
        """Формируем контекст"""
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        data = self.get_city_weather(city)
        cached = CacheService().create_cache(city=city, data=data)
        context['city'] = self.request.GET.get('city')
        return self.get_mixin_context(context, cached)

    def post(self, request, *args, **kwargs):
        """Добавление записи в БД"""
        data_weather = {
            "city": request.POST.get('name'),
            "latitude": request.POST.get('latitude'),
            "longitude": request.POST.get('longitude'),
            "user": request.user

        }
        save_location = WeatherDatabaseService(LocationsRepository()).save_location(**data_weather)

        return redirect('weather:index')


class DeleteLocation(DeleteView):
    model = Locations
    success_url = reverse_lazy('weather:index')

    def get_object(self, queryset=None):
        get_pk = self.kwargs['pk']
        user = self.request.user
        # location = Locations.objects.get(id=get_pk, userid=self.request.user)
        location = WeatherDatabaseService(LocationsRepository()).get_location(id=get_pk, userid=user)
        # Очистка кеша
        # delete_cached(location.name)
        # get_cached(location)
        # if location in cached_cities:
        #     cached_cities.remove(location)
        #     cache.set('cached_cities', cached_cities)

        return location

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        self.object = obj
        cached_cities = cache.get('cached_cities', [])
        if self.object.name in cached_cities:
            CacheService().delete_cached(self.object.name)
        self.object.delete()
        return redirect(self.success_url)
