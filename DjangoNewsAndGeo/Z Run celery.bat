celery -A DjangoNewsAndGeo worker --pool=solo --loglevel=info

@REM del celerybeat.pid

@REM celery -A DjangoNewsAndGeo beat -l info
pause