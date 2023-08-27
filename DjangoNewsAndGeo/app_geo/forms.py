from django import forms
from .widgets import MapWidget


class SightAdminForm(forms.ModelForm):
    '''
    Форма для модели Примечательного места в админ-панели
    '''
    name = forms.CharField(max_length=100, min_length=3)
    rating = forms.IntegerField(
        initial=0,
        min_value=0,
        max_value=25
    )
    latitude = forms.DecimalField(
        initial=0,
        max_digits=11,
        decimal_places=8,
        min_value=-90,
        max_value=90
    )
    longitude = forms.DecimalField(
        initial=0,
        max_digits=11,
        decimal_places=8,
        min_value=-180,
        max_value=180
    )
    map = forms.CharField(widget=MapWidget(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['map'].widget = MapWidget()
