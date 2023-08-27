from django.contrib import admin

from app_geo.models import Sight

class SightAdmin(admin.ModelAdmin):
    '''
    Административная модель для Примечательного места
    '''
    change_list_template = 'change_list.html'


    def has_add_permission(self, request):
        return False

admin.site.register(Sight, SightAdmin)