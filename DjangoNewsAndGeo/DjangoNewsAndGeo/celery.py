import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoNewsAndGeo.settings')# установает значение по умолчанию для среды DJANGO_SETTINGS_MODULE, чтобы Celery знала, как найти проект Django.

app = Celery('app_news') # создаем экземпляр Celery с именем core и поместили в переменную app.
app.config_from_object('django.conf:settings', namespace='CELERY') # загрузили значения конфигурации Celery из объекта настроек из django.conf. Мы использовали namespace=«CELERY» для предотвращения коллизий с другими настройками Django. Таким образом, все настройки конфигурации для Celery должны начинаться с префикса CELERY_.
app.autodiscover_tasks() # говорит Celery искать задания из приложений, определенных в settings.INSTALLED_APPS.

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from constance import config
    # Настройка периодических задач
    app.conf.beat_schedule = {
        # Задача для отправки новостных email
        'send_news_email': {
            'task': 'news.tasks.send_daily_email',
            'schedule': crontab(seconds=config.EMAIL_SEND_TIME.second),
        }
    }


# для тестов
@app.task
def add(x, y):
    return x / y

