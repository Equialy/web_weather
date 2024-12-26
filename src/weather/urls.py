from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.get_city_weather, name='weather_data'),
    path('weather/save/', views.save_to_db_location, name='weather_data_save'),
    path('weather/<int:pk>/', views.delete_location, name='delete_data'),
    # path('', views.Index.as_view(), name='index'),
    # path('weather/', views.GetCityWeather.as_view(), name='weather_data'),
    # path('weather/<int:pk>/', views.DeleteLocation.as_view(), name='delete_data'),


]