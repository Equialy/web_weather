FROM python:3.12-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]