@REM celery -A DjangoNewsAndGeo worker --pool=solo --loglevel=info

del celerybeat.pid

celery -A DjangoNewsAndGeo beat -l info
@REM pause