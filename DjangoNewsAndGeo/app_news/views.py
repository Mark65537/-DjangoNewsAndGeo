"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from django.http import HttpResponseRedirect

from app_news.forms import NewsForm
from app_news.models import News

class MainPage(generic.ListView):
    """Представление главной страницы, которая отображает список всех новостей"""
    model = News
    context_object_name = 'news_list'
    template_name = 'site/index.html'
    queryset = News.objects.all().order_by('-updated_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateNews(generic.CreateView):
    """Представление для создания новости"""
    model = News
    form_class = NewsForm
    template_name = 'site/create_news.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)

        if self.request.user.is_authenticated:
            self.object.author = self.request.user.profile
            self.request.user.profile.news_quantity += 1
            self.request.user.profile.save()
        else:
            self.object.author = self.request.META['REMOTE_ADDR']  # Устанавливаем автора как IP-адрес текущего пользователя

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'site/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'site/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
