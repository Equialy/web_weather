from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserRegisterForm, ProfileUserForm
import logging

from weather.models import Locations
from weather.services.weather_services import WeatherAPIService

logger = logging.getLogger('web')



class LoginUser(LoginView):
    form_class = UserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class UserProfile(LoginRequiredMixin, UpdateView, WeatherAPIService):  # GetContextAPI
    model = Locations
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        logger.debug(f"Запрос на получение пользователя {self.request}")
        return self.request.user
