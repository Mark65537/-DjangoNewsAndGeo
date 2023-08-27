import openpyxl

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from .models import Sight
from django.shortcuts import render

def geoindex(request):
    return render(request, 'geoindex.html')

def import_sights(request):
    '''
    Функция импорта Примечательных мест
    '''
    if request.method == 'POST':
        # Получение файла из запроса
        file = request.FILES["file"]
        try:
            wb = openpyxl.load_workbook(file)
            sheet = wb.active
            created = 0
            errors = []
            # Чтение файла построчно, создание и валидация объекта на основе полученных данных
            for row in sheet.iter_rows(values_only=True):
                name, latitude, longitude, rating = row[:4]
                try:
                    sight = Sight(name=name, latitude=latitude, longitude=longitude, rating=rating)
                    sight.full_clean()
                    sight.save()
                    created += 1
                except Exception as e:
                    errors.append(str(e))
            messages.success(request, f'Загружено {created} записей.')
            for error in errors:
                messages.error(request, error)
            return redirect(reverse('admin:app_geo_sight_changelist'))
        except Exception as e:
            messages.error(request, f'Ошибка обработки файла: {str(e)}')
            return redirect(reverse('admin:app_geo_sight_changelist'))
    return HttpResponse(status=405)

