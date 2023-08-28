#если возникает ошибка
#TypeError: clean() got an unexpected keyword argument 'styles'
#нужно установить старую версию Bleach:
#pip install bleach==3.3.1

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News

#admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
