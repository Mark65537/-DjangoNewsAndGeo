start "" "Z Run Redis.bat"
start "" "Z Run celery.bat"
C:\Users\Mark\AppData\Local\Yandex\YandexBrowser\Application\browser.exe http://localhost:8080/
py manage.py runserver --settings DjangoNewsAndGeo.settings 8080
