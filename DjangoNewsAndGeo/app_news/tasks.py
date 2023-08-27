from celery import shared_task
from datetime import date, timedelta
from constance import config

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import News

@shared_task
def send_news_email():
    # Получение настроек
    recipients = settings.CONSTANCE_CONFIG['EMAIL_RECIPIENTS']
    subject = settings.CONSTANCE_CONFIG['EMAIL_SUBJECT']
    message = settings.CONSTANCE_CONFIG['EMAIL_MESSAGE']

    today = date.today()

    # Получение новостей, опубликованных сегодня
    news_published_today = News.objects.filter(created_at__exact=today)
    context = {
        'message': message,
        'news': news_published_today,
    }

    # Генерация HTML-сообщения на основе шаблона и контекста
    email_message = render_to_string('daily_news_email.html', context)

    # Отправка email
    send_mail(
        subject=subject,
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        html_message=email_message,
        fail_silently=False,
    )


