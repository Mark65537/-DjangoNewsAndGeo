"""
Django settings for DjangoNewsAndGeo project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from datetime import timedelta
from celery.schedules import crontab

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4c46e207-0009-4091-a89d-a6d9374e8a33'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'app_news',
    'app_geo',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'constance',
    'constance.backends.database',
    'djeym',
    'ckeditor',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'DjangoNewsAndGeo.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoNewsAndGeo.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SUMMERNOTE
SUMMERNOTE_CONFIG = { 'iframe': True, 'summernote': { 'toolbar': [ ['style', ['style']], 
                       ['font', ['bold', 'italic', 'underline', 'clear']], 
                       ['fontname', ['fontname']], ['color', ['color']], 
                       ['para', ['ul', 'ol', 'paragraph']], ['table', ['table']], 
                       ['insert', ['link', 'picture', 'video']], 
                       ['view', ['fullscreen', 'codeview', 'help']], ], 
                       'width': '100%', 'height': '400px', }, }


# Constance config
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend' 
CONSTANCE_CONFIG = {
    'EMAIL_RECIPIENTS': ('test@mail.ru', 'Список адресатов через пробел'),
    'EMAIL_SUBJECT': ('Новости за сегодня', 'Тема сообщения'),
    'EMAIL_MESSAGE': ('Ознакомьтесь с последними новостями', 'Текст сообщения'),
    'EMAIL_SEND_TIME': (timedelta(seconds=20), 'Время отправки'),
}
CONSTANCE_CONFIG_FIELDSETS = {
    'Настройки отправки email с новостями за день': ('EMAIL_RECIPIENTS', 'EMAIL_SUBJECT', 'EMAIL_MESSAGE', 'EMAIL_SEND_TIME'),
}

# Celery config
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"  # URL брокера сообщений Celery, При развертывании в production рекомендуется использовать более мощные и масштабируемые брокеры сообщений, такие как RabbitMQ или Redis.
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"  # URL бэкэнда для хранения результатов задач Celery

# Дополнительные настройки Celery...
CELERY_BEAT_SCHEDULE = { 
    'send_news_email_task': { 
        'task': 'app_news.tasks.send_news_email',
        'schedule': crontab(minute="*/1"),
    },
}

# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False


# django-ckeditor
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'djeym.utils.get_filename'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # False - Only image files. (At your discretion)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    },
    'djeym': {
        'toolbar': 'full',
        'height': 400,
        'width': 362,
        'colorButton_colors': 'F44336,C62828,E91E63,AD1457,9C27B0,6A1B9A,'
                              '673AB7,4527A0,3F51B5,283593,2196F3,1565C0,'
                              '03A9F4,0277BD,00BCD4,00838F,009688,00695C,'
                              '4CAF50,2E7D32,8BC34A,558B2F,CDDC39,9E9D24,'
                              'FFEB3B,F9A825,FFC107,FF8F00,FF9800,EF6C00,'
                              'FF5722,D84315,795548,4E342E,607D8B,37474F,'
                              '9E9E9E,424242,000000,FFFFFF',
        'colorButton_enableAutomatic': False,
        'colorButton_enableMore': True
    }
}


# The API key is used in the free and paid versions.
# You can get the key in the developer’s office - https://passport.yandex.com/
# ( API-ключ используется в свободной и платной версиях.
#   Получить ключ можно в кабинете разработчика - https://developer.tech.yandex.ru/ )
DJEYM_YMAPS_API_KEY = os.getenv('API_KEY')

# For paid use API --> True
# ( Для платного использования --> True )
DJEYM_YMAPS_API_KEY_FOR_ENTERPRISE = False

# Map download mode. Default = 'release'
# (Режим загрузки карт.)
# DJEYM_YMAPS_DOWNLOAD_MODE = 'debug'

