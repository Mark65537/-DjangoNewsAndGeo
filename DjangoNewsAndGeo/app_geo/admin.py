from django.contrib import admin
from django.http import FileResponse

from openpyxl import Workbook

from .forms import SightAdminForm
from .models import Sight, WeatherSummary

@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    '''
    Административная модель для Примечательного места
    '''
    change_list_template = 'change_list.html'
    form = SightAdminForm

    def has_add_permission(self, request):
        return False


class SightFilter(admin.SimpleListFilter):
    '''
    Фильтр для Сводок погоды по Примечательному месту
    '''
    template = 'sight-filter.html'
    title = 'Примечательное место'
    parameter_name = 'sight_id__exact'

    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        sights = queryset.values_list('sight__id', 'sight__name').distinct()
        return sights

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(sight_id=int(self.value()))
        return queryset

@admin.register(WeatherSummary)
class WeatherSummaryAdmin(admin.ModelAdmin):
    '''
    Административная модель для Сводок погоды
    '''
    actions = ['export_summaries']
    date_hierarchy = 'timestamp'
    list_filter = [SightFilter]
    readonly_fields = ('sight', 'timestamp', 'temperature', 'humidity', 'pressure', 'wind_direction', 'wind_speed')

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)
    
    def has_add_permission(self, request):
        return False
    
    #def has_delete_permission(self, request, obj=None):
    #    return False

    @admin.action(description="Экспортировать сводки погоды")
    def export_summaries(self, request, selected):
        '''
        Функция экспорта сводок погоды
        '''
        workbook = Workbook()
        sheet = workbook.active
        # Запись заголовков в файл
        sheet.append(field.verbose_name for field in WeatherSummary._meta.fields if field.name != 'id')
        # Запись сериализованных объектов в файл
        for summary in selected:
            serialized_data = summary.serialize()
            sheet.append(serialized_data[key] for key in serialized_data)
        buffer = io.BytesIO()
        workbook.save(buffer)
        buffer.seek(0)
        # Возврат ответа в виде xslx-файла
        return FileResponse(buffer, as_attachment=True, filename='summaries.xlsx')

#admin.site.register(Sight, SightAdmin)