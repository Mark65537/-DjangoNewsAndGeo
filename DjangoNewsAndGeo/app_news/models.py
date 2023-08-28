"""
Definition of models.
"""

from django.db import models
from django.urls import reverse
from django_summernote.fields import SummernoteTextField

class News(models.Model):
    """Модель новости"""
    title = models.CharField(max_length=200, verbose_name='Title')
    description = SummernoteTextField()
    image = models.ImageField(upload_to='static\images', blank=True)
    author = author = models.CharField(max_length=100, default='Anonymous', verbose_name='Author')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="News"
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')
