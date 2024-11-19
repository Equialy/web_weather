from django.urls import path
from . import views
app_name = 'weather'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('weather/', views.GetCityWeather.as_view(), name='weather_data'),
    path('weather/<int:pk>/', views.DeleteLocation.as_view(), name='delete_data'),

]