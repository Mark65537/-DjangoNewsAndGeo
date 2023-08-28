@echo off
@REM py manage.py shell -c "from DjangoNewsAndGeo.celery import add;add.delay(8, 2)"
@REM py manage.py shell -c "from app_news.tasks import send_news_email;send_news_email()"
py manage.py shell -c "from app_geo.tasks import fetch_weather_data;fetch_weather_data()"
pause