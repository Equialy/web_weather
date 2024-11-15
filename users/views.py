from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserRegisterForm, ProfileUserForm



# Create your views here.

class LoginUser(LoginView):
    form_class = UserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}



class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name =  'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class UserProfile(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user

