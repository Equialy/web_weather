from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('users/', include('users.urls', namespace='users')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

