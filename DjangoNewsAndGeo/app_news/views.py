"""
Definition of views.
"""

from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from django.urls import reverse_lazy

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


class UpdateNews(generic.UpdateView):
    """Представление, для обновления новости"""
    model = News
    form_class = NewsForm
    template_name = 'site/update_news.html'

    #override form_valid method
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)   


class DeleteNews(generic.DeleteView):
    """Представление, для удаления новости"""
    model = News
    template_name = 'site/delete_news.html'
    success_url = reverse_lazy('index') # здесь используется reverse_lazy, таким образом пользователь не будет перенаправлен до тех пор, пока представление не завершит удаление записи из базы данных.


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
