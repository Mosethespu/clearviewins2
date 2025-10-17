FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install django
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
