from celery import shared_task
from datetime import date, timedelta

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import News

@shared_task
def send_news_email():
    today = date.today()

    # ѕолучение новостей, опубликованных сегодн€
    news_published_today = News.objects.filter(publication_date__exact=today)
    context = {
        'message': message,
        'news': news_published_today,
    }

    # √енераци€ HTML-сообщени€ на основе шаблона и контекста
    email_message = render_to_string('daily_news_email.html', context)

    recipients = settings.CONSTANCE_CONFIG['EMAIL_RECIPIENTS']
    subject = settings.CONSTANCE_CONFIG['EMAIL_SUBJECT']
    message = settings.CONSTANCE_CONFIG['EMAIL_MESSAGE']

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)


