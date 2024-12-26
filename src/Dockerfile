FROM python:3.12-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

COPY docker/entrypoint.sh /usr/src/app/entrypoint.sh
COPY ../requirements.txt /usr/src/app
#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#COPY . /app
#WORKDIR /app

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]