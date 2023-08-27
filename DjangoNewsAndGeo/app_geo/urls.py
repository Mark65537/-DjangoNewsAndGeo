from django.urls import path
from . import views

urlpatterns = [
    path('', views.geoindex, name='geoindex'),
    path('sight/import/', views.import_sights, name='import_sights'),
]

