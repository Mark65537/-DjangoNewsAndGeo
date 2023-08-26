import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')# ���������� �������� �� ��������� ��� ����� DJANGO_SETTINGS_MODULE, ����� Celery �����, ��� ����� ������ Django.

app = Celery('core') # ������� ��������� Celery � ������ core � ��������� � ���������� app.
app.config_from_object('django.conf:settings', namespace='CELERY') # ��������� �������� ������������ Celery �� ������� �������� �� django.conf. �� ������������ namespace=�CELERY� ��� �������������� �������� � ������� ����������� Django. ����� �������, ��� ��������� ������������ ��� Celery ������ ���������� � �������� CELERY_.
app.autodiscover_tasks() # ������� Celery ������ ������� �� ����������, ������������ � settings.INSTALLED_APPS.

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from constance import config
    # ��������� ������������� �����
    app.conf.beat_schedule = {
        # ������ ��� �������� ��������� email
        'send_news_email': {
            'task': 'news.tasks.send_daily_email',
            'schedule': crontab(second=config.EMAIL_SEND_TIME.second),
        }
    }

