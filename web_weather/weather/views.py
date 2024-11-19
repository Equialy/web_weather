from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView
from weatherapp import settings
from .models import Locations
from .save_locations.save_handler import SaveLocations
from .weather_utils import WeatherMixinAPI, GetContextAPI
from .service_handler import handlers


class Index(ListView, WeatherMixinAPI):
    template_name = 'weather/index_home.html'
    title_page = 'Главная страница'
    context_object_name = 'location_data'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Locations.objects.filter(userid=self.request.user)
        else:
            return Locations.objects.none()


class GetCityWeather(TemplateView, GetContextAPI):
    template_name = 'weather/weather.html'
    model = Locations

    def get_context_data(self, **kwargs):
        """Формируем контекст"""
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        data = self.get_city_weather(city)
        context['city'] = self.request.GET.get('city')
        return self.get_mixin_context(context, data)

    def post(self, request, *args, **kwargs):
        """Добавление записи в БД"""

        city = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        SaveLocations()
        location = Locations.objects.create(name=city, latitude=latitude, longitude=longitude, userid=request.user)
        location.save()

        return redirect('weather:index')


class DeleteLocation(DeleteView):
    model = Locations
    success_url = reverse_lazy('weather:index')
