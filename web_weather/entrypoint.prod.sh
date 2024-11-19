#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres еще не запущен..."

    # Проверяем доступность хоста и порта
    while ! nc -z $PG_HOST -p $PG_PORT; do
      sleep 10
    done

    echo "PostgreSQL запущен"
fi

exec "$@"