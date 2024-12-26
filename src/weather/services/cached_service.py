from django.core.cache import cache


class CacheService:
    def __init__(self):
        self._time_cache = 30

    def create_cache(self, city, data):
        """Создание или обновление кеша для города."""
        cache.set(f'cached_city_{city}', data, timeout=self._time_cache)
        return data

    def get_cached(self, city):
        """ Получение данныхиз кеша """
        return cache.get(f'cached_city_{city}')

    def delete_cached(self, city):
        """Удаление данных города из кеша."""
        cache.delete(f'cached_city_{city}')
