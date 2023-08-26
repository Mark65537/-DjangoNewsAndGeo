@echo off
py manage.py shell -c "from DjangoNewsAndGeo.celery import add;result = add.delay(8, 2)"
py manage.py shell -c "from app_news.tasks import send_news_email;send_news_email()"

pause