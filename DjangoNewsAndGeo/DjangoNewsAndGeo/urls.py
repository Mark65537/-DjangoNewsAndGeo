"""
Definition of urls for DjangoNewsAndGeo.
"""

from datetime import datetime

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page

from app_news import forms, views
from app_news.views import CreateNews, DeleteNews, MainPage, UpdateNews, DetailNews

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('geoindex/', views.geoindex, name='geoindex'),
    path('<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('create_news/', cache_page(3600)(CreateNews.as_view()), name='create_news'),
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    path('delete_news/<int:pk>/', DeleteNews.as_view(), name='delete_news'),
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
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djeym/', include('djeym.urls', namespace='djeym')),
    path('summernote/', include('django_summernote.urls')),
]
