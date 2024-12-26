#!/bin/bash


echo "Запуск миграций..."
python manage.py migrate --noinput


echo "Cборка статики..."
python manage.py collectstatic --noinput


echo "Запуск сервера..."
exec "$@"