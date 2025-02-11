from DjangoNewsAndGeo.settings import DJEYM_YMAPS_API_KEY
from django.templatetags.static import static
from django import forms


class MapWidget(forms.Widget):
    '''
    Виджет карты для моделей Примечательных мест в админ-панели
    '''
    media = forms.Media(
        js=(f'https://api-maps.yandex.ru/2.1/?apikey={DJEYM_YMAPS_API_KEY}&lang=ru-RU',
            static('app/scripts/map.js')))
    template_name = 'map_field.html'

    def __init__(self, attrs=None):
        super().__init__(attrs=attrs)
