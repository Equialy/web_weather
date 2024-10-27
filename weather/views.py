from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from weatherapp import settings
from .models import Locations
from .weather_utils import WeatherMixin
from .service_handler import handlers


class Index( ListView):
    template_name = 'weather/index_home.html'
    title_page = 'Главная страница'
    context_object_name = 'location_data'



    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Locations.objects.filter(userid=self.request.user)
        else:
            return Locations.objects.none()

class GetCityWeather(TemplateView, WeatherMixin):
    template_name = 'weather/weather.html'
    model = Locations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        data = self.get_city_weather(city)
        context['city'] = self.request.GET.get('city')
        context['weather_data'] = data
        context['temp_min'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['temp_min'])
        context['temp_max'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['temp_max'])
        context['current_temp'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['feels_like'])
        context['feels_like'] = handlers.kelvins_to_celsious(self.extra_context['weather_data']['main']['feels_like'])
        context['get_lon'] = round(self.extra_context['weather_data']['coord']['lat'], 5)
        context['get_lat'] = round(self.extra_context['weather_data']['coord']['lon'], 5)

        return context

    def post(self, request, *args, **kwargs):
        """Добавление записи в БД"""
        city = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        location = Locations.objects.create(name=city, latitude=latitude, longitude=longitude, userid=request.user)
        location.save()
        return redirect('weather:index')


class DeleteLocation(DeleteView):
    model = Locations
    success_url = reverse_lazy('weather:index')



