# WeatherApp

WeatherApp — это веб-приложение на базе Django, которое позволяет пользователям просматривать текущую погоду для любых местоположений. Также приложение включает в себя функционал для регистрации и аутентификации пользователей.

## Возможности

- **Текущая информация о погоде**: Пользователи могут просматривать погоду для любого города с помощью OpenWeatherMap API.
- **Аутентификация пользователей**: Регистрация и вход в систему с возможностью сохранять местоположения и предпочтения.
- **Социальная аутентификация**: Вход через сторонние сервисы, такие как Google и GitHub, с использованием Django Social Auth.
- **Адаптивный дизайн**: Интерфейс, построенный с использованием Bootstrap 5, адаптирован для мобильных устройств.
- **База данных**: PostgreSQL для хранения данных, включая учетные записи пользователей и местоположения.



### Установка
**Клонируйте репозиторий**:
 git clone https://github.com/Equialy/web_weather.git

### Использование Docker-compose
Для использование Docker-compose выполните следующие шаги:

Для работы с PostgreSQL укажите настройки подключения в файле .env Например:

- PG_NAME=weatherapp
- PG_USER=yourusername
- PG_PASSWORD=yourpassword
- PG_HOST=localhost
- PG_PORT=5432


**Указать переменные в .env**:
- API_KEY   "Для работы с API" апи используются с сайта https://openweathermap.org/
- SECRET_KEY
- CSRF_TRUSTED_ORIGINS
- DEBUG=True
- ALLOWED_HOSTS

Для работы с аутентификацией зарегестрировать приложение на GoogleCloud и прописать переменные для:
- GOOGLE_OAUTH2_KEY
- GOOGLE_OAUTH2_SECRET
Для аутентификации по GitGub:
- GITHUB_KEY
- GITHUB_SECRET

**Запустить Docker-compose**:

- docker-compose -f docker-compose.prod.yml up -d --build 
- docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
- docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
- Октрыть в браузере по адресу http://127.0.0.1/


