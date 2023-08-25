"""
Definition of urls for DjangoNewsAndGeo.
"""

from datetime import datetime

from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page

from app_news import forms, views
from app_news.views import CreateNews, MainPage, UpdateNews

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('create_news/', cache_page(3600)(CreateNews.as_view()), name='create_news'),
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='site/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
