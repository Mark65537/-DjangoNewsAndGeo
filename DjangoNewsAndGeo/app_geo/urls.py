from django.urls import path
from . import views

urlpatterns = [
    path('', views.geoindex, name='geoindex'),
]

